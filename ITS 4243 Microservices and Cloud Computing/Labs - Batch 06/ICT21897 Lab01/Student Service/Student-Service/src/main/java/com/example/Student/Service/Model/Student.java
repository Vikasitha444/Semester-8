package com.example.Student.Service.Model;

import jakarta.persistence.*;

@Entity
@Table(name = "students")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;
    private String course;  // මේක add කරන්න
    private Integer age;    // මේක add කරන්න

    // Constructors
    public Student() {}

    public Student(String name, String email) {
        this.name = name;
        this.email = email;
    }

    // Getters and Setters
    public Long getId() { return id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getCourse() { return course; }      // මේක add කරන්න
    public void setCourse(String course) { this.course = course; }  // මේක add කරන්න

    public Integer getAge() { return age; }           // මේක add කරන්න
    public void setAge(Integer age) { this.age = age; }  // මේක add කරන්න
}