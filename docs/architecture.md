# TripPilot Architecture

## 1. Current Architecture

TripPilot is a FastAPI-based travel planning application.

The application currently follows a layered architecture:

```text
Frontend
    |
    | HTTP / JSON
    v
FastAPI Application
    |
    v
API Routes
    |
    v
Service Layer
    |
    v
SQLAlchemy Models
    |
    v
PostgreSQL
```

## 2. Application Entry Point

The application starts from:

app/main.py

Responsibilities of main.py:

Load environment configuration
Create the FastAPI application
Initialize database metadata
Register API routers
Serve the frontend
Expose application health information

The HTTP resource routes are intentionally kept outside main.py.

3. API Layer

API routes are implemented in:

app/api/routes.py

The API router currently uses the /api prefix.

Responsibilities of the API layer:

Define HTTP endpoints
Receive request parameters
Validate request bodies through Pydantic schemas
Obtain the database session
Call the appropriate service
Return the service result

The API layer should not contain database implementation details or complex business logic.

4. Service Layer

Business and persistence operations currently live in:

app/services/

Examples:

trip_service.py
flight_service.py
hotel_service.py
activity_service.py
itinerary_service.py

The service layer is responsible for:

Creating application entities
Querying application entities
Performing application-level operations
Coordinating database operations
Supporting itinerary generation and AI workflows
5. Database Layer

Database configuration currently lives in:

app/database.py

SQLAlchemy is used as the ORM.

The current database flow is:

API Route
    |
    v
Service
    |
    v
SQLAlchemy ORM
    |
    v
PostgreSQL
6. Dependency Management

Database sessions are currently provided through FastAPI dependency injection:

db: Session = Depends(get_db)

The database dependency is currently located in:

app/api/routes.py

This will later be moved into a dedicated dependency module as part of the dependency-boundary and security refactoring.

7. Why Routes Were Moved Out of main.py

Previously, app/main.py contained:

FastAPI initialization
Database setup
Database dependency
All API routes
Service imports
AI endpoints

This created unnecessary coupling.

The first architecture refactor moved the HTTP routes into:

app/api/routes.py

As a result:

main.py
    -> application startup and registration

routes.py
    -> HTTP/API interface

services/
    -> application operations

models/
    -> database representation

This improves separation of concerns and gives TripPilot a structure that can be expanded without continually increasing the size of main.py.

8. Current API Resources

TripPilot currently exposes resources for:

Trips
Flights
Hotels
Activities
Itinerary items
Trip summaries
AI trip context
Generated itineraries
AI-generated itineraries
9. Curriculum Topics Covered

This architecture step implements the following curriculum topics:

MVC Architecture
Models in MVC
Views in MVC
Controllers
Routes in REST APIs
Services in MVC
Dependency Boundaries in MVC
Separation of Concerns
Modular Project Structure
FastAPI Project Architecture

Not all MVC concepts are implemented as separate classes yet. The current structure establishes the foundation and will be refined incrementally.

10. Tools and Libraries

Current technologies involved in this architecture:

Python
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
Uvicorn
python-dotenv
HTML/CSS/JavaScript
Git
GitHub
11. Verification

The architecture refactor was verified with:

curl http://127.0.0.1:8000/api/health

and:

curl http://127.0.0.1:8000/api/trips

The FastAPI Swagger UI was also verified at:

http://127.0.0.1:8000/docs

The existing TripPilot data remained accessible after the refactor.
