package com.example.Course.service.Model;


import jakarta.persistence.*;

@Entity
@Table(name="courses")

public class Course {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;
    private String description;

    // Constructors
    public Course() {}

    public Course(String title, String description) {
        this.title = title;
        this.description = description;
    }

    // Getters & setters
    public Long getId() { return id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description;}

}
