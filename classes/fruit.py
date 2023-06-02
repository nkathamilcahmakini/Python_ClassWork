class Fruits:
    category = "Fresh fruits"
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def eat(self):
        return f"Sally is eating a {self.color} {self.name}"
    
    def remove(self):
        return f"Makena is removing the seeds of a {self.name}"
    
    def tastes(self):
        return f"Favour is eating a {self.taste} {self.name}"