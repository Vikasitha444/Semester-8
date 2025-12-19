# Result Service

Spring Boot microservice to manage student grades.

## Overview
- Runs on port **8084**
- Database: **MySQL (`resultservicedb`)**

## How to Run
1. Create database:

   CREATE DATABASE resultservicedb;

2. Set database credentials in `application.properties`.
3. Run:


## Endpoints

### POST /results
Add a result for a student.

**Request Body:**
```json
{
"studentId": 1,
"courseId": 2,
"grade": "A"
}
```
GET /results/student/{id}
- Get results of a specific student.