class Country:
    def __init__ (self, name, population, area):
        self.name=name
        self.population=population
        self.area=area

    def is_larger(self, other):
        if (self.area>other.area):
            return True
        else:
            return False
    def population_desity(self):
        return self.population/self.area

    def __str__ (self):
        return ('{} has a population of {} and is {} sqare km'.format(self.name, self.population, self.area))

    def __repr__(self):
        return ("Country('{0}', {1}, {2})".format(self.name, self.population, self.area))

# a
canada = Country("Canada", 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)
print(canada.name)
print(canada.population)
print(canada.area)
# b
print(canada.is_larger(usa))
print(usa.is_larger(canada))
# c
print(canada.population_desity())
# d
usa = Country('United States of America', 313914040, 9826675)
print(usa)
# e
canada = Country('Canada', 34482779, 9984670)
print(canada)
print([canada])
