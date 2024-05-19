#!/usr/bin/env python

from user import User

import random


class Teacher(User): # teacher is a subclass of User, initialize with first and last name.

    def __init__(self, first_name , last_name):
        super().__init__(first_name, last_name) # supercharged User class's init method
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]  


    def teach(self):
        random_index = random.randint(0, len(self.knowledge) - 1) # random index with random.randint() method
        # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
        return self.knowledge[random_index]
            
        
my_teacher = Teacher("my", "teacher")
print(my_teacher.knowledge) # returns the list
print(my_teacher.teach())  # picks random element in the list