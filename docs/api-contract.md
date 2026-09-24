# TripPilot API Contract

## 1. API Overview

TripPilot exposes a REST-style HTTP API through FastAPI.

Base URL during local development:

    http://127.0.0.1:8000

Current API prefix:

    /api

Interactive API documentation is available through FastAPI Swagger UI:

    http://127.0.0.1:8000/docs

OpenAPI specification:

    http://127.0.0.1:8000/openapi.json

## 2. Trip Resources

### Create Trip

    POST /api/trips

Creates a new trip.

Request body:

    {
      "name": "Goa Weekend",
      "destination": "Goa",
      "start_date": "2026-11-20",
      "end_date": "2026-11-23",
      "travelers": 2,
      "budget": 50000,
      "currency": "INR"
    }

### List Trips

    GET /api/trips

Returns all trips currently stored in the database.

## 3. Flight Resources

### Add Flight

    POST /api/trips/{trip_id}/flights

Adds a flight to a trip.

### List Flights

    GET /api/trips/{trip_id}/flights

Returns flights associated with a trip.

## 4. Hotel Resources

### Add Hotel

    POST /api/trips/{trip_id}/hotels

Adds a hotel booking to a trip.

### List Hotels

    GET /api/trips/{trip_id}/hotels

Returns hotels associated with a trip.

## 5. Activity Resources

### Add Activity

    POST /api/trips/{trip_id}/activities

Adds an activity to a trip.

### List Activities

    GET /api/trips/{trip_id}/activities

Returns activities associated with a trip.

## 6. Itinerary Resources

### Add Itinerary Item

    POST /api/trips/{trip_id}/itinerary

Adds an itinerary item to a trip.

### List Itinerary

    GET /api/trips/{trip_id}/itinerary

Returns itinerary items ordered by activity date and start time.

## 7. Trip Intelligence

### Trip Summary

    GET /api/trips/{trip_id}/summary

Returns a summary of the trip and its associated data.

### AI Trip Context

    GET /api/trips/{trip_id}/ai-context

Builds the structured context used by the AI itinerary workflow.

## 8. Itinerary Generation

### Generate Deterministic Itinerary

    POST /api/trips/{trip_id}/generate-itinerary

Generates an itinerary using TripPilot's deterministic itinerary engine.

### Generate AI Itinerary

    POST /api/trips/{trip_id}/generate-ai-itinerary

Generates an itinerary using the AI itinerary workflow.

The AI workflow currently includes:

1. Context preparation
2. Gemini generation
3. Validation
4. Persistence

## 9. Application Health

### Health Check

    GET /api/health

Returns the current application health status and environment.

Example response:

    {
      "status": "healthy",
      "environment": "development"
    }

## 10. HTTP Methods Currently Used

TripPilot currently uses:

- GET for retrieving resources
- POST for creating resources and triggering generation operations

Additional REST methods such as PUT, PATCH, and DELETE will be introduced as the API evolves.

## 11. Request Validation

Request bodies are validated using Pydantic schemas.

Current schemas include:

    app/schemas/
    ├── trip.py
    ├── flight.py
    ├── hotel.py
    ├── activity.py
    ├── itinerary.py
    ├── ai_context.py
    └── ai_itinerary.py

FastAPI automatically exposes validation errors through the generated OpenAPI contract.

## 12. Current Response Strategy

The current API returns SQLAlchemy model objects or service-generated response data.

A future API-contract refactor will introduce dedicated response schemas where appropriate.

This will provide:

- Stable response contracts
- Explicit API serialization
- Better control over exposed fields
- Consistent API versioning
- Cleaner separation between database models and API responses

## 13. Current API Architecture

The request flow is:

    HTTP Request
         |
         v
    FastAPI Router
         |
         v
    Pydantic Validation
         |
         v
    Service Layer
         |
         v
    SQLAlchemy
         |
         v
    PostgreSQL
         |
         v
    HTTP Response

The API layer is intentionally kept separate from the service layer.

## 14. API Design Topics Covered

The current implementation establishes the foundation for:

- REST APIs
- Resources in REST APIs
- HTTP Methods
- URI Design
- Path Parameters
- Request Bodies
- Response Bodies
- Request Validation
- FastAPI/OpenAPI
- Service Layer Integration
- API Documentation

The following topics will be added in later phases:

- Query Parameters
- Pagination
- Filtering
- Sorting
- API Versioning
- Standardized Error Formats
- Authentication
- Authorization
- Rate Limiting
- External API Integration
- Webhooks
