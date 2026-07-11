# SentinelX AI
## REST API Specification

---

# 1. Introduction

SentinelX AI exposes a RESTful API that enables communication between the backend services, the Web Dashboard, external applications, and future third-party integrations.

The API follows REST principles and returns JSON responses.

---

# 2. API Architecture

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
```

---

# 3. Authentication

Authentication Method

JWT (JSON Web Token)

Authorization Header

Authorization: Bearer <token>

---

# 4. Response Format

Successful Response

```json
{
    "success": true,
    "message": "Operation completed successfully.",
    "data": {}
}
```

Error Response

```json
{
    "success": false,
    "message": "Resource not found.",
    "errors": []
}
```

---

# 5. Authentication Endpoints

## Login

POST

/api/v1/auth/login

Request

- username
- password

Response

- Access Token
- Refresh Token

---

## Logout

POST

/api/v1/auth/logout

---

## Refresh Token

POST

/api/v1/auth/refresh

---

## Current User

GET

/api/v1/auth/me

---

# 6. User Management

Get Users

GET

/api/v1/users

---

Get User

GET

/api/v1/users/{id}

---

Create User

POST

/api/v1/users

---

Update User

PUT

/api/v1/users/{id}

---

Delete User

DELETE

/api/v1/users/{id}

---

# 7. Alert Management

Get Alerts

GET

/api/v1/alerts

---

Get Alert

GET

/api/v1/alerts/{id}

---

Delete Alert

DELETE

/api/v1/alerts/{id}

---

Filter Alerts

GET

/api/v1/alerts/filter

---

# 8. Incident Management

Get Incidents

GET

/api/v1/incidents

---

Create Incident

POST

/api/v1/incidents

---

Update Incident

PUT

/api/v1/incidents/{id}

---

Close Incident

PATCH

/api/v1/incidents/{id}/close

---

# 9. Detection Engine

Predict Attack

POST

/api/v1/detection/predict

---

Prediction History

GET

/api/v1/detection/history

---

Detection Statistics

GET

/api/v1/detection/statistics

---

# 10. Risk Assessment Engine

Evaluate Risk

POST

/api/v1/risk/evaluate

---

Get Risk Assessment

GET

/api/v1/risk/{id}

---

Risk Statistics

GET

/api/v1/risk/statistics

---

# 11. Decision Engine

Generate Decision

POST

/api/v1/decision/evaluate

---

Decision History

GET

/api/v1/decision/history

---

Decision Details

GET

/api/v1/decision/{id}

---

# 12. Prevention Engine

Recommend Prevention

POST

/api/v1/prevention/recommend

---

Execute Prevention

POST

/api/v1/prevention/execute

---

Prevention History

GET

/api/v1/prevention/history

---

# 13. Learning Engine

Update Knowledge

POST

/api/v1/learning/update

---

Retrain Model

POST

/api/v1/learning/retrain

---

Learning Statistics

GET

/api/v1/learning/statistics

---

# 14. Knowledge Base

Get Knowledge

GET

/api/v1/knowledge

---

Knowledge Details

GET

/api/v1/knowledge/{id}

---

Create Knowledge

POST

/api/v1/knowledge

---

Update Knowledge

PUT

/api/v1/knowledge/{id}

---

Delete Knowledge

DELETE

/api/v1/knowledge/{id}

---

# 15. Machine Learning Models

Get Models

GET

/api/v1/models

---

Upload Model

POST

/api/v1/models

---

Activate Model

PATCH

/api/v1/models/{id}/activate

---

Delete Model

DELETE

/api/v1/models/{id}

---

# 16. Dashboard

Dashboard Statistics

GET

/api/v1/dashboard/statistics

---

Real-Time Metrics

GET

/api/v1/dashboard/live

---

System Status

GET

/api/v1/dashboard/status

---

# 17. Audit Logs

Get Logs

GET

/api/v1/logs

---

Export Logs

GET

/api/v1/logs/export

---

# 18. Health Monitoring

Health Check

GET

/api/v1/health

---

Version

GET

/api/v1/version

---

# 19. HTTP Status Codes

200 OK

201 Created

204 No Content

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

422 Validation Error

500 Internal Server Error

---

# 20. API Security

JWT Authentication

HTTPS

Role-Based Access Control (RBAC)

Input Validation

Rate Limiting

Audit Logging

CORS Protection

---

# 21. API Versioning

Current Version

v1

Future Versions

v2

v3

Backward compatibility shall be maintained whenever possible.

---

# 22. Future API Features

GraphQL

WebSockets

Streaming Events

Webhook Notifications

OpenAPI Client SDK

---

# 23. Conclusion

The SentinelX AI REST API provides a secure, modular, and scalable interface that connects every intelligent engine of the platform while remaining extensible for future integrations.

---

Document Version: 1.0

Status: Approved

Last Update: July 2026