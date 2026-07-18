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