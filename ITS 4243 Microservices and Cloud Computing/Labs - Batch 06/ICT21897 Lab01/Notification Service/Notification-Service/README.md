# Notification Service

Simple Spring Boot microservice to print enrollment notifications.

## Overview
- Runs on port **8085**
- Prints messages to console when a student enrolls
- Database is optional (used only for GET endpoints)
- Called by Enrollment Service

## How to Run
Run the service:

## Endpoints

---

### **POST /notify/enrollment**
Print enrollment message to console.

**Request Body:**
```json
{
  "studentId": 1,
  "courseId": 2
}
```
Response:
```json
"Student 1 enrolled into Course 2"

```