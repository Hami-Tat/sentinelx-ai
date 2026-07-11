# SentinelX AI
## Software Requirements & Functional Specification
### Project Specification (Cahier des Charges)



# 1. Project Overview

## Project Name

SentinelX AI

## Project Type

Intelligent Cyber Defense Platform

## Version

1.0

## Project Status

In Development



# 2. Context

Cyber attacks are becoming increasingly sophisticated and frequent. Traditional Intrusion Detection Systems (IDS) are capable of detecting malicious activities but rely heavily on human analysts to interpret alerts and decide on appropriate responses.

This approach suffers from several limitations:

- Alert fatigue
- High false positive rates
- Delayed incident response
- Limited automation
- Lack of continuous learning

SentinelX AI addresses these limitations by introducing Artificial Intelligence into every stage of the cyber defense lifecycle.



# 3. Problem Statement

Organizations require cybersecurity systems capable of:

- Detecting attacks in real time.
- Understanding the severity of attacks.
- Recommending intelligent responses.
- Preventing attacks before damage occurs.
- Learning continuously from previous incidents.

Traditional IDS solutions only solve the first problem.

SentinelX AI solves the entire decision-making process.



# 4. Project Objectives

## Main Objective

Develop an intelligent cyber defense platform capable of detecting, assessing, preventing, and learning from cyber threats.



## Specific Objectives

- Capture live network traffic.
- Extract network features.
- Detect malicious activities using Machine Learning.
- Assess cyber risks.
- Recommend security decisions.
- Execute preventive actions.
- Learn from previous incidents.
- Continuously improve detection models.
- Provide an interactive monitoring dashboard.
- Store historical knowledge for future analysis.

---

# 5. Functional Scope

The first version includes:

- Network Traffic Capture
- Feature Extraction
- Intrusion Detection Engine
- Risk Assessment Engine
- Decision Engine
- Prevention Engine
- Learning Engine
- Knowledge Base
- REST API
- PostgreSQL Database
- Web Dashboard
- Logging System



# 6. System Actors

The system interacts with:

- Security Analyst
- Network Administrator
- System Administrator
- Machine Learning Engineer
- Researcher



# 7. Functional Modules

## Module 1

Network Collector

Responsibilities:

- Capture packets
- Build network flows
- Filter traffic



## Module 2

Feature Extraction

Responsibilities:

- Extract statistical features
- Normalize data
- Prepare ML input



## Module 3

Detection Engine

Responsibilities:

- Predict attacks
- Classify attack categories
- Produce confidence scores



## Module 4

Risk Assessment Engine

Responsibilities:

- Calculate risk score
- Estimate impact
- Prioritize threats



## Module 5

Decision Engine

Responsibilities:

- Apply security policies
- Recommend response strategies
- Validate prevention actions



## Module 6

Prevention Engine

Responsibilities:

- Block malicious IPs
- Isolate hosts
- Update firewall rules
- Execute preventive actions



## Module 7

Learning Engine

Responsibilities:

- Learn from incidents
- Improve models
- Detect concept drift
- Update Knowledge Base



## Module 8

Knowledge Base

Responsibilities:

- Store incidents
- Store attack signatures
- Store prevention strategies
- Store model history



## Module 9

REST API

Responsibilities:

- Authentication
- Data access
- Alert management
- Dashboard communication



## Module 10

Dashboard

Responsibilities:

- Visualize alerts
- Display statistics
- Monitor system health
- Manage prevention actions



# 8. System Architecture

SentinelX AI follows Clean Architecture.

Presentation Layer

↓

Application Layer

↓

Domain Layer

↓

Infrastructure Layer

Each layer is isolated and independently testable.



# 9. Business Workflow

Network Traffic

↓

Network Collector

↓

Feature Extraction

↓

Detection Engine

↓

Risk Assessment

↓

Decision Engine

↓

Prevention Engine

↓

Learning Engine

↓

Knowledge Base

↓

Dashboard

---

# 10. Machine Learning Workflow

Dataset

↓

Preprocessing

↓

Training

↓

Validation

↓

Model Evaluation

↓

Model Storage

↓

Real-Time Prediction

↓

Continuous Learning



# 11. Database Responsibilities

Store:

- Alerts
- Incidents
- Network Flows
- Users
- Models
- Logs
- Knowledge Base



# 12. Performance Requirements

Detection latency:

< 100 ms

System availability:

> 99%

Prediction accuracy target:

> 98%

False Positive Rate:

< 2%


# 13. Security Requirements

- JWT Authentication
- Password Hashing
- HTTPS Support
- Audit Logs
- Role-Based Access Control
- Data Encryption



# 14. Technical Stack

Programming Language

Python

Backend

FastAPI

Machine Learning

Scikit-Learn

Database

PostgreSQL

ORM

SQLAlchemy

Visualization

Chart.js

Containerization

Docker

Testing

Pytest

Code Quality

Ruff

Version Control

Git + GitHub



# 15. Deliverables

The project shall deliver:

- Complete source code
- UML diagrams
- REST API
- Web Dashboard
- Machine Learning models
- PostgreSQL schema
- Technical documentation
- User documentation
- Test reports
- Deployment guide



# 16. Project Constraints

- Python ≥ 3.12
- PostgreSQL
- Cross-platform compatibility
- Open-source technologies only
- Modular architecture
- High maintainability



# 17. Acceptance Criteria

The project will be accepted if:

✓ Network traffic is captured successfully.

✓ ML models detect attacks accurately.

✓ Risk scores are correctly generated.

✓ Prevention recommendations are produced.

✓ Knowledge Base updates automatically.

✓ Dashboard displays live information.

✓ REST API functions correctly.

✓ Unit tests pass.

✓ Documentation is complete.



# 18. Project Roadmap

Sprint 0

Project Setup

Sprint 1

Domain Layer

Sprint 2

Knowledge Base

Sprint 3

Network Collector

Sprint 4

Feature Extraction

Sprint 5

Detection Engine

Sprint 6

Risk Assessment Engine

Sprint 7

Decision Engine

Sprint 8

Prevention Engine

Sprint 9

Learning Engine

Sprint 10

REST API

Sprint 11

Dashboard

Sprint 12

Testing & Deployment



# 19. Future Evolution

Future versions may include:

- Federated Learning
- Deep Learning
- Reinforcement Learning
- SIEM Integration
- Cloud Deployment
- Multi-Agent Collaboration
- Explainable AI
- Distributed Sensors



# 20. Conclusion

SentinelX AI is designed as an intelligent cyber defense platform that goes beyond traditional intrusion detection systems.

By integrating Machine Learning, risk assessment, automated prevention, and continuous learning into a unified architecture, SentinelX AI provides a modern approach to proactive cybersecurity.

The platform serves as both an academic research project and a production-ready foundation for future intelligent cybersecurity systems.



**Document Version:** 1.0

**Status:** Approved

**Last Update:** July 2026