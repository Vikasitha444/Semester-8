# Course Service

Spring Boot microservice to manage courses.

## Overview
- Runs on port **8082**
- Database: **MySQL (`courseservicedb`)**
- Provides CRUD operations for courses.

## How to Run
1. Create database:

CREATE DATABASE courseservicedb;

2. Update `application.properties` with MySQL username/password.
3. Run:


## Endpoints

### GET /courses
Retrieve all courses.

**Example Response:**
```json
[
{"id":1, "title":"Math", "description":"Mathematics"},
{"id":2, "title":"Physics", "description":"Physics basics"}
]
```
POST /courses

Create a new course.

Request Body:
```json
{
"title": "Chemistry",
"description": "Organic Chemistry"
}
```
GET /courses/{id}

Retrieve a course by ID.

Example Response:
```
{
"id": 1,
"title": "Math",
"description": "Mathematics"
}
```
