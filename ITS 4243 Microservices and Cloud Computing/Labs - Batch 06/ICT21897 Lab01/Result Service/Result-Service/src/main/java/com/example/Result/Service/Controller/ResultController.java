package com.example.Result.Service.Controller;

import com.example.Result.Service.Model.Result;
import com.example.Result.Service.Repository.ResultRepository;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/results")
public class ResultController {

    private final ResultRepository repo;

    public ResultController(ResultRepository repo) { this.repo = repo; }

    @PostMapping
    public ResponseEntity<Result> addResult(@RequestBody Map<String, Object> request) {
        Long studentId = Long.valueOf(request.get("studentId").toString());
        Long courseId = Long.valueOf(request.get("courseId").toString());
        String grade = request.get("grade").toString();

        Result result = new Result(studentId, courseId, grade);
        return ResponseEntity.ok(repo.save(result));
    }

    @GetMapping("/student/{studentId}")
    public ResponseEntity<List<Result>> getStudentResults(@PathVariable Long studentId) {
        List<Result> results = repo.findByStudentId(studentId);
        if(results.isEmpty()) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(results);
    }
}
