package com.example.Course.service.Controller;

import com.example.Course.service.Model.Course;
import com.example.Course.service.Repository.CourseRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/courses")
public class CourseController {

    private final CourseRepository repo;

    public CourseController(CourseRepository repo) {
        this.repo = repo;
    }

    @GetMapping
    public List<Course> getAllCourses() {
        return repo.findAll();
    }

    @PostMapping
    public Course createCourse(@RequestBody Course course) {
        return repo.save(course);
    }

    @GetMapping("/{id}")
    public Course getCourseById(@PathVariable Long id) {
        return repo.findById(id)
                .orElseThrow(() -> new RuntimeException("Course not found with id: " + id));
    }
}
