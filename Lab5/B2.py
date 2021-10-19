from B1 import Country    
class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

    def total_population(self):
        total = 0
        for country in self.countries:
            total = total + country.population
        return total

    def __str__(self):
        res = self.name
        for country in self.countries:
            res = res + '\n' + str(country)
        return res       

canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040,9826675)
mexico = Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)
# a
print(north_america.name)
for country in north_america.countries:
    print(country)
# b
print(north_america.total_population())
# c
print(north_america)
