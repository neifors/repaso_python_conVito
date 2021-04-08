
class Country():
    
    population_sum = 0.0
    
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population
        Country.population_sum += self.population
        
    def __str__(self):
        return f'\nCountry: {self.name}**\n**Capital: {self.capital}'