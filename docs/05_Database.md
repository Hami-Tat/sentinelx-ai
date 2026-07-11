# SentinelX AI
## Database Design



# 1. Introduction

SentinelX AI uses PostgreSQL as its primary relational database.

The database is responsible for storing operational data, machine learning metadata, historical cyber incidents, prevention actions, and the cybersecurity knowledge base.

The design follows normalization principles while remaining optimized for real-time cybersecurity operations.



# 2. Objectives

The database must:

- Store captured network flows.
- Store alerts and detected attacks.
- Store incidents.
- Store prevention actions.
- Store security decisions.
- Store machine learning models.
- Store users and roles.
- Maintain the Knowledge Base.
- Preserve complete audit logs.



# 3. Database Architecture

```
                PostgreSQL
                     │
 ┌───────────────────┼───────────────────┐
 │                   │                   │
 Operational      Knowledge         Administration
 Database           Base               Data
```



# 4. Main Entities

The platform stores information about:

- Users
- Roles
- Network Flows
- Alerts
- Threats
- Incidents
- Risk Assessments
- Decisions
- Prevention Actions
- Machine Learning Models
- Knowledge Base
- Audit Logs



# 5. Tables

## users

Purpose

Store authenticated users.

Fields

- id
- username
- email
- password_hash
- role_id
- created_at



## roles

Purpose

Store user roles.

Fields

- id
- name
- description

Examples

- Administrator
- Security Analyst
- Researcher



## network_flows

Purpose

Store captured network flows.

Fields

- id
- source_ip
- destination_ip
- source_port
- destination_port
- protocol
- packet_count
- byte_count
- duration
- timestamp



## alerts

Purpose

Store every detected alert.

Fields

- id
- flow_id
- attack_type
- confidence_score
- risk_score
- status
- created_at



## incidents

Purpose

Store confirmed security incidents.

Fields

- id
- alert_id
- severity
- description
- analyst_notes
- resolved
- created_at



## threats

Purpose

Threat catalog.

Fields

- id
- name
- category
- description
- mitigation



## risk_assessments

Purpose

Store calculated risks.

Fields

- id
- incident_id
- likelihood
- impact
- risk_score
- calculated_at



## decisions

Purpose

Store decisions produced by the Decision Engine.

Fields

- id
- incident_id
- decision
- reason
- confidence
- created_at

Examples

- Ignore
- Monitor
- Alert
- Block
- Quarantine



## prevention_actions

Purpose

Store executed prevention actions.

Fields

- id
- decision_id
- action
- target
- execution_status
- executed_at

Examples

- Block IP
- Block Port
- Disable Service
- Firewall Update



## ml_models

Purpose

Store Machine Learning model metadata.

Fields

- id
- model_name
- algorithm
- version
- accuracy
- precision
- recall
- f1_score
- trained_at



## model_predictions

Purpose

Store prediction history.

Fields

- id
- model_id
- flow_id
- prediction
- confidence
- prediction_time



## knowledge_base

Purpose

Store cybersecurity knowledge.

Fields

- id
- threat_id
- lesson
- recommendation
- created_at



## audit_logs

Purpose

Store all important system actions.

Fields

- id
- user_id
- action
- object
- timestamp

---

# 6. Entity Relationships

```
Users
 │
 └──── Roles

NetworkFlows
 │
 └──── Alerts
        │
        └──── Incidents
                │
                ├──── Risk Assessments
                │
                ├──── Decisions
                │       │
                │       └──── Prevention Actions
                │
                └──── Knowledge Base

ML Models
 │
 └──── Model Predictions
```



# 7. Indexes

Indexes should be created on:

- source_ip
- destination_ip
- timestamp
- attack_type
- severity
- risk_score



# 8. Constraints

Examples

- email must be unique
- username must be unique
- confidence_score between 0 and 1
- risk_score between 0 and 100



# 9. Audit Strategy

Every important action performed by:

- User
- Decision Engine
- Prevention Engine
- Learning Engine

must be recorded.



# 10. Data Retention

Recommended retention:

Alerts

90 days

Incidents

5 years

Audit Logs

5 years

Knowledge Base

Permanent

Machine Learning Models

Permanent



# 11. Future Extensions

Future versions may include:

- Threat Intelligence feeds
- Malware samples
- IOC database
- MITRE ATT&CK mapping
- CVE database
- Distributed sensors
- Multi-tenant support



# 12. Conclusion

The SentinelX AI database is designed to support both operational cybersecurity activities and continuous machine learning improvement.

The schema allows the platform to evolve from a traditional IDS into a complete AI-powered cyber defense platform capable of learning from historical events and improving future security decisions.



Document Version: 1.0

Status: Approved

Last Update: July 2026