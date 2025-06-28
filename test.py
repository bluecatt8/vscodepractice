
from dataclasses import dataclass
from typing import List, Dict
print("hello world!")
print("just run it and dont ask questions")
print("this is a test")
mylist = [1, 2, 3, 4, 5]
mymap = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
for i in mylist:
    print(i)


@dataclass
class Person:
    name: str
    age: int
    team_preference: str
    team_morale: int


    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def cheer(self) -> str:
        return f"Go {self.team_preference}!"

@dataclass 
class stadium_class:
    team_capacity: List[int]
    team_names: List[str]
    location: str
    capacity: int
    def __init__(self, name: str, capacity: int, location: str, teams: List[str]):
        self._name = name
        self._capacity = capacity
        self._location = location
        self._teams = teams

class stadium:

    def __init__(self, name: str):
        
    @property
    def name(self) -> str:
        return self._name
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def location(self) -> str:

    @property
    def teams(self) -> List[str]:
        return self._teams
    
    @staticmethod
    def get_stadium_name() -> str:
        return "Stadium Name"
    
    
    @staticmethod
    def add_person(self, person: Person) -> None:
        print(f"Adding {person.name} to the stadium.")

