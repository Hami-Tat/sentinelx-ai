# SentinelX AI
# Architecture de Référence v1.0

**Document :** 04_Architecture_v1.md

**Projet :** SentinelX AI – Intelligent Cyber Defense Platform

**Version :** 1.0

**Statut :** Architecture officielle

**Auteur :** Équipe SentinelX AI

---

# 1. Vision

SentinelX AI est une plateforme intelligente de cyberdéfense capable de surveiller un réseau en temps réel, détecter des cyberattaques connues et inconnues grâce au Machine Learning, évaluer le niveau de risque, prendre des décisions automatiques et proposer des mécanismes de prévention.

Contrairement aux IDS traditionnels, SentinelX AI possède son propre moteur de capture réseau et ne dépend d'aucune solution tierce comme Suricata.

L'objectif est de construire une plateforme entièrement autonome, évolutive, modulaire et extensible.

---

# 2. Objectifs

Les objectifs principaux sont :

- Capturer le trafic réseau en temps réel
- Décoder les protocoles réseau
- Construire les flux de communication
- Extraire les caractéristiques utiles
- Détecter les comportements malveillants
- Détecter les attaques Zero-Day
- Évaluer le niveau de risque
- Décider automatiquement des actions
- Exécuter des mécanismes de prévention
- Apprendre continuellement de nouveaux comportements

---

# 3. Principes d'Architecture

SentinelX AI est construit selon les principes suivants.

## Domain Driven Design (DDD)

Toute la logique métier est indépendante des bibliothèques externes.

Le domaine représente le cœur du système.

---

## Clean Architecture

Les dépendances pointent toujours vers le domaine.

Infrastructure → Application → Domaine

Jamais l'inverse.

---

## Single Responsibility Principle

Chaque module possède une seule responsabilité.

---

## Open / Closed Principle

Le système doit pouvoir être étendu sans modifier les composants existants.

---

## Modularité

Chaque moteur est indépendant.

---

## Testabilité

Tous les composants doivent être testables indépendamment.

---

# 4. Architecture Générale

```
                        Utilisateur
                               │
                               ▼
                    Dashboard Web
                               │
                               ▼
                           REST API
                               │
                               ▼
                    Application Services
                               │
                               ▼
                    Core Detection Platform
                               │
        ┌──────────────┬───────────────┬───────────────┐
        ▼              ▼               ▼
 Capture Engine   Processing Engine  Detection Engine
        │              │               │
        └──────────────┴───────────────┘
                       │
                       ▼
               Decision Platform
                       │
                       ▼
               Prevention Platform
                       │
                       ▼
               Learning Platform
```

---

# 5. Architecture du Core

Le Core est composé des moteurs suivants.

## 5.1 Capture Engine

Responsabilités

- Capture réseau
- Gestion des interfaces
- Gestion des buffers
- Capture temps réel

Entrée

Interface réseau

Sortie

Paquets bruts

---

## 5.2 Packet Decoder

Responsabilités

- Ethernet
- ARP
- IPv4
- IPv6
- TCP
- UDP
- ICMP

Entrée

Paquets bruts

Sortie

Packet Entity

---

## 5.3 Flow Engine

Responsabilités

- Reconstruction des sessions
- Identification des flux
- Timeout
- Statistiques

Sortie

Flow Entity

---

## 5.4 Feature Engine

Responsabilités

Extraction des caractéristiques.

Exemples

- durée
- nombre de paquets
- débit
- taille moyenne
- flags TCP
- entropy
- ratio entrant/sortant

---

## 5.5 Detection Engine

Responsabilités

Détection des cyberattaques.

Modèles prévus

- Random Forest
- Isolation Forest
- One-Class SVM
- AutoEncoder
- Deep Learning

Sortie

Threat Entity

---

## 5.5.1 Calibration et Agrégation des Scores de Confiance

Problème

Les modèles prévus ne produisent pas des sorties comparables. Random Forest et Deep Learning (supervisés) sortent une probabilité par classe (`predict_proba` / softmax) sur [0,1], mais pas nécessairement bien calibrée. Isolation Forest et One-Class SVM (anomalie) sortent un score d'anomalie ou une distance à la frontière de décision. AutoEncoder sort une erreur de reconstruction. Aucune de ces trois échelles n'est une probabilité au sens statistique.

Comparer ces sorties brutes entre elles pour choisir "la confiance la plus élevée" n'a pas de sens : un score d'anomalie élevé n'indique pas la même chose qu'une probabilité de classe élevée. Cette confusion se propagerait jusqu'au Risk Engine (5.7), puisque `Threat.confidence` alimente directement le `RiskScore`.

Étape 1 — Calibration par détecteur

Chaque `Detector` doit produire une confiance calibrée dans `DetectionResult` (interprétable comme "probabilité que la prédiction soit correcte"), jamais sa sortie brute.

- Détecteurs supervisés (Random Forest, Deep Learning) : calibration Platt scaling ou isotonic regression sur les probabilités brutes, validée par reliability diagram / Brier score sur le jeu de validation.
- Détecteurs d'anomalie (Isolation Forest, One-Class SVM) : transformation sigmoïde du score d'anomalie, ajustée sur la distribution des scores observée sur le jeu de validation (trafic normal vs attaques connues).
- AutoEncoder : transformation de l'erreur de reconstruction via une sigmoïde centrée sur un seuil de reconstruction appris (`confidence = sigmoid(k * (erreur - seuil))`).

Les paramètres de calibration (seuils, coefficients) sont propres à chaque version de modèle. Ils sont ré-entraînés et revalidés à chaque cycle du Learning Engine (5.10), en même temps que le modèle qu'ils calibrent.

Étape 2 — Agrégation pondérée

`EnsembleManager` n'effectue pas une simple sélection de la confiance maximale. Il agrège les résultats calibrés selon deux rôles distincts :

- Les détecteurs supervisés identifient un `ThreatType` précis avec leur confiance calibrée.
- Les détecteurs d'anomalie ne connaissent pas de catégorie précise : ils ne font que signaler un comportement anormal. Leur rôle est de corroborer (ou contredire) le type proposé par les détecteurs supervisés, et de capter les attaques Zero-Day que le supervisé n'a jamais vues à l'entraînement.

Règle d'agrégation :

1. Poids par détecteur = `MLModel.accuracy` (déjà présent dans l'entité domaine), normalisé entre les seuls détecteurs disponibles (`is_available() == True`) ; les détecteurs indisponibles sont exclus et leur poids redistribué.
2. Pour un `ThreatType` proposé par un ou plusieurs détecteurs supervisés, la confiance finale est la moyenne pondérée de leurs confidences calibrées, renforcée (pondération additive bornée) par tout signal de corroboration provenant des détecteurs d'anomalie.
3. Si aucun détecteur supervisé ne propose de type mais qu'un ou plusieurs détecteurs d'anomalie signalent une anomalie forte, le résultat est classé `ThreatType.ZERO_DAY` avec la confiance d'anomalie pondérée.
4. Un seuil de décision configurable s'applique avant transmission au Risk Engine. En dessous de ce seuil, le résultat est classé `ThreatType.UNKNOWN` et escaladé pour revue humaine plutôt que transmis automatiquement au Decision Engine.

Sortie

`DetectionResult` agrégé (confiance calibrée et pondérée), prêt à alimenter le Risk Engine (5.7).

---

## 5.6 Knowledge Base

Responsabilités

- enrichissement
- contexte
- recommandations

---

## 5.7 Risk Engine

Responsabilités

Calcul du Risk Score.

Sortie

RiskAssessment

---

## 5.8 Decision Engine

Responsabilités

Choisir automatiquement la meilleure réponse.

---

## 5.9 Prevention Engine

Responsabilités

- blocage IP
- blacklist
- isolation machine
- limitation de trafic
- génération de règles

---

## 5.10 Learning Engine

Responsabilités

- apprentissage continu
- mise à jour des modèles
- validation
- versionnement

---

# 6. Architecture Applicative

```
Frontend

Dashboard

        │

REST API

        │

Application Layer

        │

Domain Layer

        │

Infrastructure
```

---

# 7. Dashboard

Le Dashboard constitue le SOC de SentinelX AI.

Fonctionnalités

- tableau de bord
- trafic temps réel
- incidents
- alertes
- chronologie
- recherche
- statistiques
- cartes
- administration
- configuration
- utilisateurs
- rapports
- monitoring

---

# 8. Site Web

Le site institutionnel est indépendant du Dashboard.

Pages prévues

Accueil

Fonctionnalités

Documentation

Téléchargement

Tarifs

Blog

Contact

Support

---

# 9. API

L'API constitue le point d'entrée de la plateforme.

Fonctionnalités

- REST
- JWT
- OAuth2
- OpenAPI
- Documentation Swagger

---

# 10. Base de Données

SGBD

PostgreSQL

Tables principales

users

roles

permissions

packets

flows

alerts

threats

incidents

risk_assessments

knowledge

ml_models

system_logs

audit_logs

network_interfaces

settings

---

# 11. Architecture Docker

```
Docker Compose

┌──────────────────────┐
│ sentinelx-core       │
└──────────────────────┘

┌──────────────────────┐
│ sentinelx-api        │
└──────────────────────┘

┌──────────────────────┐
│ sentinelx-dashboard  │
└──────────────────────┘

┌──────────────────────┐
│ postgres             │
└──────────────────────┘

┌──────────────────────┐
│ redis                │
└──────────────────────┘
```

---

# 12. Structure du Projet

```
src/

sentinelx_ai/

domain/

application/

capture_engine/

packet_decoder/

flow_engine/

feature_engine/

detection_engine/

risk_engine/

decision_engine/

prevention_engine/

learning_engine/

api/

dashboard/
```

---

# 13. Flux de Données

```
Carte réseau

↓

Capture Engine

↓

Packet Decoder

↓

Flow Engine

↓

Feature Engine

↓

Detection Engine

↓

Knowledge Base

↓

Risk Engine

↓

Decision Engine

↓

Prevention Engine

↓

Learning Engine

↓

Dashboard

↓

Utilisateur
```

---

# 14. Sécurité

Authentification

JWT

RBAC

Journalisation

Audit

HTTPS

Hash des mots de passe

Chiffrement des secrets

---

# 15. Qualité Logicielle

Pytest

Ruff

GitHub Actions

Pre-commit

Tests unitaires

Tests d'intégration

Documentation

---

# 16. Déploiement

Développement

Docker Compose

Production

Docker

Reverse Proxy

HTTPS

CI/CD

---

# 17. Évolutions Futures

Version 2

- Cluster
- Agents distribués
- Haute disponibilité

Version 3

- IA Générative
- Threat Intelligence
- Réponse autonome

Version 4

- Multi-tenant
- Cloud Native
- Kubernetes
- Federation

---

# 18. Règles d'Or du Projet

Aucun moteur ne doit dépendre directement d'un autre.

Toutes les communications passent par des interfaces.

Aucune logique métier dans l'infrastructure.

Toutes les fonctionnalités doivent être testées.

Chaque Sprint suit le cycle :

Développement

Tests

Pytest

Ruff

Commit

Push

Une seule responsabilité par module.

L'architecture ne sera modifiée qu'après validation technique.