package com.example.Notification.Service.Controller;

import com.example.Notification.Service.Model.Notification;
import com.example.Notification.Service.Repository.NotificationRepository;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/notify")
public class NotificationController {

    private final NotificationRepository repo;

    public NotificationController(NotificationRepository repo) {
        this.repo = repo;
    }

    // Create notification (called by Enrollment Service)
    @PostMapping("/enrollment")
    public String notifyEnrollment(@RequestBody Map<String, Object> request) {
        Long studentId = Long.valueOf(request.get("studentId").toString());
        Long courseId = Long.valueOf(request.get("courseId").toString());

        String message = "Student " + studentId + " enrolled into Course " + courseId;
        System.out.println(message);
        return message;
    }

    // Get all notifications
    @GetMapping
    public ResponseEntity<List<Notification>> getAllNotifications() {
        return ResponseEntity.ok(repo.findAll());
    }

    // Get notifications by studentId
    @GetMapping("/student/{studentId}")
    public ResponseEntity<List<Notification>> getStudentNotifications(@PathVariable Long studentId) {
        List<Notification> notifications = repo.findByStudentId(studentId);
        if(notifications.isEmpty()) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(notifications);
    }
}
