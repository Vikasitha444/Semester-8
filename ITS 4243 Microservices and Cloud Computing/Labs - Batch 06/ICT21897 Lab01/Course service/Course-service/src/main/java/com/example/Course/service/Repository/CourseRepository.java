package com.example.Course.service.Repository;

import com.example.Course.service.Model.Course;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CourseRepository extends JpaRepository<Course,Long>{

        }