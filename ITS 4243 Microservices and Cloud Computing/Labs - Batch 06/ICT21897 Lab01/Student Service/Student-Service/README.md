# Student Service

Spring Boot microservice to manage students.

## Overview
- Runs on port **8081**
- Database: **MySQL (`studentservicedb`)**
- Provides CRUD operations for students.

## How to Run
1. Create database:

CREATE DATABASE studentservicedb;

2. Update `application.properties` with your MySQL username/password.
3. Run:



## Endpoints

### GET /students
Retrieve all students.

**Example Response:**
```json
[
{"id":1, "name":"himasha", "email":"himasha@gmail.com"},
{"id":2, "name":"bimasha", "email":"bimasha@gmail.com"}
]
```
POST /students

Create a new student.

Request Body:
```json
{
"name": "himasha",
"email": "himasha@gmail.com"
}
```
GET /students/{id}

Retrieve a student by ID.

Example Response:
```json
{
  "id": 1,
  "name": "himasha",
  "email": "himasha@gmail.com"
}
```