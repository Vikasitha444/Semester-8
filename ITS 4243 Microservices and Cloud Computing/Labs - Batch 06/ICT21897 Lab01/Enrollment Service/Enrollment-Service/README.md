
# Enrollment Service

Spring Boot microservice to manage enrollments.

## Overview
- Runs on port **8083**
- Database: **MySQL (`enrollmentservicedb`)**
- Validates student + course IDs by calling Student and Course services.
- Calls Notification Service after successful enrollment.

## How to Run
1. Create database:

   CREATE DATABASE enrollmentservicedb;

2. Update MySQL username/password in `application.properties`.
3. Ensure Student + Course + Notification services are running.
4. Run:


## Endpoints

### POST /enroll
Enroll a student in a course.

**Request Body:**
```json
{
"studentId": 1,
"courseId": 2
}
```
Example Response:
```json
{
"id": 1,
"studentId": 1,
"courseId": 2,
"enrolledAt": "2025-11-19T10:45:00"
}
```
