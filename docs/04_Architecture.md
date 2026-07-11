# SentinelX AI
## Software Architecture



# 1. Introduction

SentinelX AI follows a modular, scalable and maintainable architecture based on the principles of:

- Clean Architecture
- Domain-Driven Design (DDD)
- Event-Driven Architecture
- SOLID Principles

The architecture separates business logic from infrastructure to facilitate testing, maintenance, scalability and future evolution.



# 2. Architectural Vision

Unlike traditional IDS solutions, SentinelX AI is organized around intelligent cyber defense engines.

The platform continuously observes, analyzes, decides, prevents and learns from cyber events.

The system is designed to support future integration of new Machine Learning models, prevention strategies and autonomous decision-making capabilities.



# 3. Architectural Principles

The architecture follows these principles:

- Separation of Concerns
- Dependency Inversion
- Single Responsibility
- High Cohesion
- Low Coupling
- Testability
- Extensibility
- Security by Design



# 4. Global Architecture

```
                Web Dashboard
                      │
                      ▼
               REST API (FastAPI)
                      │
                      ▼
            Application Layer
                      │
                      ▼
               Domain Layer
                      │
                      ▼
          Infrastructure Layer
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 PostgreSQL                  Network Collector
                              (Scapy/Suricata)
```

The Domain Layer is the heart of the platform.

No external framework may contain business logic.



# 5. Clean Architecture

SentinelX AI is organized into four layers.

## Presentation Layer

Responsibilities:

- REST API
- Authentication
- Dashboard communication
- HTTP Requests
- Response formatting

Technologies:

- FastAPI
- Pydantic



## Application Layer

Responsibilities:

- Application services
- Use Cases
- Command Handlers
- Query Handlers
- Orchestration

The Application Layer coordinates the business workflow.



## Domain Layer

Responsibilities:

- Business Rules
- Entities
- Value Objects
- Domain Events
- Repository Interfaces
- Domain Services

This layer contains no dependency on:

- FastAPI
- PostgreSQL
- SQLAlchemy
- Machine Learning libraries



## Infrastructure Layer

Responsibilities:

- Database
- ORM
- File Storage
- Machine Learning Models
- Network Capture
- External Services



# 6. Domain Model

The Domain Layer contains the following business concepts:

Entities

- Alert
- Incident
- Threat
- PreventionAction
- Decision
- Knowledge
- ModelVersion
- NetworkFlow

Value Objects

- IPAddress
- Port
- RiskScore
- ConfidenceScore
- Timestamp
- Protocol

Repositories

- AlertRepository
- KnowledgeRepository
- ThreatRepository
- ModelRepository

Domain Services

- DetectionService
- RiskAssessmentService
- DecisionService
- PreventionService
- LearningService



# 7. Cyber Defense Engines

SentinelX AI is composed of five intelligent engines.

## Detection Engine

Responsibilities:

- Intrusion Detection
- Attack Classification

Input

Network Features

Output

Threat Prediction



## Risk Assessment Engine

Responsibilities

- Threat Severity
- Business Impact
- Risk Score



## Decision Engine

Responsibilities

- Policy Evaluation
- Action Selection
- Decision Validation



## Prevention Engine

Responsibilities

- Block IP
- Block Port
- Quarantine Host
- Firewall Update



## Learning Engine

Responsibilities

- Continuous Learning
- Knowledge Base Update
- Model Retraining
- Drift Detection



# 8. Knowledge Base

The Knowledge Base stores:

- Historical attacks
- Prevention strategies
- Detection statistics
- Security policies
- Lessons learned
- Model metadata

Every engine can consult the Knowledge Base.

Only the Learning Engine can update it.



# 9. Event-Driven Communication

The engines communicate using Domain Events.

Examples:

AttackDetected

↓

RiskCalculated

↓

DecisionTaken

↓

PreventionExecuted

↓

KnowledgeUpdated

This approach reduces coupling between modules.



# 10. Data Flow

```
Packet

↓

Collector

↓

Feature Extraction

↓

Detection

↓

Risk Assessment

↓

Decision

↓

Prevention

↓

Learning

↓

Knowledge Base

↓

Dashboard
```



# 11. Directory Structure

```
src/
└── sentinelx_ai/
    ├── application/
    ├── domain/
    ├── infrastructure/
    ├── presentation/
    └── shared/
```



# 12. Design Patterns

SentinelX AI uses:

- Repository Pattern
- Factory Pattern
- Strategy Pattern
- Observer Pattern
- Dependency Injection
- Command Pattern



# 13. Scalability

The architecture supports future integration of:

- Multiple ML models
- Cloud deployment
- Distributed sensors
- Multi-agent systems
- Explainable AI
- SIEM integration



# 14. Architectural Benefits

- High maintainability
- Easy testing
- Clear separation of concerns
- Technology independence
- Scalable design
- Future-proof architecture



# 15. Conclusion

The architecture of SentinelX AI is designed to provide a robust foundation for an intelligent cyber defense platform.

By combining Clean Architecture, Domain-Driven Design and Event-Driven communication, the platform remains modular, maintainable and extensible while supporting advanced Machine Learning capabilities.



Document Version: 1.0

Status: Approved

Last Update: July 2026