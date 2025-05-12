#!/usr/bin/env python3

"""
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
"""

class Dog:
    def move(self):
        return "Walk"
class Bird:
    def move(self):
        return "Fly"

for animals in [Dog(), Bird()]:
    print(animals.move())
