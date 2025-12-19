package com.example.Enrollment.Service.Controller;

import com.example.Enrollment.Service.Model.Enrollment;
import com.example.Enrollment.Service.Repository.EnrollmentRepository;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/enroll")
public class EnrollmentController {

    private final EnrollmentRepository repo;
    private final RestTemplate restTemplate;

    public EnrollmentController(EnrollmentRepository repo) {
        this.repo = repo;
        this.restTemplate = new RestTemplate();
    }

    // Add Enrollment
    @PostMapping
    public ResponseEntity<?> addEnrollment(@RequestBody Map<String, Long> request) {
        Long studentId = request.get("studentId");
        Long courseId = request.get("courseId");

        // Validate Student
        try {
            restTemplate.getForObject("http://localhost:8081/students/" + studentId, Object.class);
        } catch (RestClientException e) {
            return ResponseEntity.badRequest().body("Invalid Student ID");
        }

        // Validate Course
        try {
            restTemplate.getForObject("http://localhost:8082/courses/" + courseId, Object.class);
        } catch (RestClientException e) {
            return ResponseEntity.badRequest().body("Invalid Course ID");
        }

        // Save Enrollment
        Enrollment enrollment = new Enrollment(studentId, courseId);
        Enrollment saved = repo.save(enrollment);

        // Notify Notification Service (optional)
        try {
            restTemplate.postForEntity(
                    "http://localhost:8085/notify/enrollment",
                    request,
                    String.class
            );
        } catch (RestClientException e) {
            System.out.println("Notification failed: " + e.getMessage());
        }

        return ResponseEntity.ok(saved);
    }

    // Get all enrollments
    @GetMapping
    public ResponseEntity<List<Enrollment>> getAllEnrollments() {
        List<Enrollment> enrollments = repo.findAll();
        return ResponseEntity.ok(enrollments);
    }

    // Get enrollment by ID
    @GetMapping("/{id}")
    public ResponseEntity<Enrollment> getEnrollmentById(@PathVariable Long id) {
        return repo.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // Get enrollments by student ID
    @GetMapping("/student/{studentId}")
    public ResponseEntity<List<Enrollment>> getStudentEnrollments(@PathVariable Long studentId) {
        List<Enrollment> enrollments = repo.findByStudentId(studentId);
        if (enrollments.isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(enrollments);
    }

    // (Optional) Get enrollments by course ID
    @GetMapping("/course/{courseId}")
    public ResponseEntity<List<Enrollment>> getCourseEnrollments(@PathVariable Long courseId) {
        List<Enrollment> enrollments = repo.findByCourseId(courseId);
        if (enrollments.isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(enrollments);
    }
}
