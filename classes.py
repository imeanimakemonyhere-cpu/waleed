#getting better in python.....................................................



from __future__ import annotations
from dataclasses import dataclass, field 
from abc import ABC, abstractmethod
import math 
from typing import Iterable 

class Shape(ABC):
    """Abstract base shape. Subclasses must provide an area property"""
    @property
    @abstractmethod
    def area(self):
        ...

    def __repr__(self):
        return f"<{self.__class__.__name__}>" 

@dataclass
class Circle(Shape):
    radius: float = field(default=0.0)

    def __post_init__(self):
        if self.radius < 0:
            raise ValueError("radius must be non-negative")

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"Circle(radius={self.radius})" 
    
@dataclass 
class Square(Shape):
    side: float = field(default=0.0)

    def __post_init__(self):
        if self.side < 0:
            raise ValueError("side must be non-negative")
    
    @property
    def area(self):
        return self.side ** 2

    def __repr__(self):
        return f"Square(side={self.side})"

@dataclass
class Triangle(Shape):
    base: float = field(default=0.0)
    height: float = field(default=0.0)

    def __post_init__(self):
        if self.base < 0 or self.height < 0 :
            raise ValueError("base and height must be non-negative")
    @property
    def area(self):
        return 0.5 * self.base * self.height
        
    def __repr__(self):
        return f"traingle(base={self.base}, height={self.height})"
    
@dataclass
class Pizza(Circle):
    toppings: Iterable[str] = field(default_factory=tuple)

    def __repr__(self):
        tops = ", ".join(self.toppings) if self.toppings else "plain"
        return f"Pizza(radius={self.radius}, toppings=[{tops}])"
    
if __name__ == "__main__":
    shapes: list[Shape] = [
        Circle(4),
        Square(5),
        Triangle(6, 7),
        Pizza(8, ("cheese", "oregano")),
    ]    
    for shape in shapes:
        print(f"Type: {type(shape).__name__}")
        print(f"   {shape!r}")
        print(f"    Area: {shape.area:.2f} cm²")
        print()
