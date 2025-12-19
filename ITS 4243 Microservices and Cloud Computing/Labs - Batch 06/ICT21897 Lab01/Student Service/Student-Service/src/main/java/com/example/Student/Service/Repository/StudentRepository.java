package com.example.Student.Service.Repository;



import com.example.Student.Service.Model.Student;
import org.springframework.data.jpa.repository.JpaRepository;


public interface StudentRepository extends JpaRepository<Student, Long> {

}