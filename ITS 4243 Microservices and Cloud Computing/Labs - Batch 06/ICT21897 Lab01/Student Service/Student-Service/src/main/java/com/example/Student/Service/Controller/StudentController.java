package com.example.Student.Service.Controller;

import com.example.Student.Service.Model.Student;
import com.example.Student.Service.Repository.StudentRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/students")

public class StudentController {

    private final StudentRepository repo;
    public StudentController(StudentRepository repo) { this.repo = repo; }

    @GetMapping
    public List<Student> getAll() { return repo.findAll(); }

    @PostMapping
    public Student create(@RequestBody Student s) {
        return repo.save(s);
    }

    @GetMapping("/{id}")
    public Student getById(@PathVariable Long id) {
        return repo.findById(id).orElseThrow(() -> new RuntimeException("Student not found"));
}

}
