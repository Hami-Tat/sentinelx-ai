# SentinelX AI
## Development Guide

---

# Development Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.14 |
| API | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Machine Learning | Scikit-Learn |
| Packet Capture | Scapy |
| Container | Docker |
| Version Control | Git + GitHub |

---

# Project Structure

```text
src/
└── sentinelx_ai/
    ├── application/
    ├── domain/
    ├── infrastructure/
    ├── presentation/
    └── shared/
```

---

# Git Workflow

```
develop
    │
    ├── feature/domain
    ├── feature/database
    ├── feature/ml-engine
    └── feature/dashboard
```

Never develop directly on **main**.

---

# Branch Naming

| Type | Example |
|------|---------|
| Feature | feature/detection-engine |
| Bug Fix | fix/api-authentication |
| Refactor | refactor/domain-services |
| Documentation | docs/update-readme |

---

# Commit Convention

| Type | Example |
|------|---------|
| feat | feat: implement detection engine |
| fix | fix: resolve packet parser bug |
| docs | docs: update architecture guide |
| refactor | refactor: simplify repositories |
| test | test: add risk engine tests |
| ci | ci: configure GitHub Actions |
| chore | chore: update dependencies |

---

# Code Style

- Follow PEP 8
- Use type hints
- Maximum line length: 88
- Prefer composition over inheritance
- Keep functions short

---

# Testing

Every new feature must include:

- Unit tests
- Integration tests (if applicable)

Minimum Coverage:

**80%**

---

# Pull Request Checklist

- Code builds successfully
- Tests pass
- Ruff passes
- Documentation updated
- No sensitive data committed

---

# Development Principles

- Clean Architecture
- Domain-Driven Design
- SOLID Principles
- Security by Design
- Test-Driven Development (when appropriate)

---

Document Version: 1.0
Status: Approved