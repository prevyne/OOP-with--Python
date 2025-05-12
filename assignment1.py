#!/usr/bin/env python3

"""
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
"""

class Superhuman:
    def __init__(self, real_name, power, signature):
        self.real_name=real_name
        self.power=power
        self.signature=signature

class Superhero(Superhuman):
    pass;
batman=Superhero("Bruce Wayne", "Tech wizardry", "Batarang")
print(f"Real name: {batman.real_name}, Power: {batman.power}, Signature: {batman.signature}")
