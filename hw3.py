# Part 1
# Purpose: take a list of objects of class CountyDemographics and return the total 2014 population from all counties
# Input: list of objects of class CountyDemographics
# Output: integer (total pop)
from bdb import effective

from data import CountyDemographics

def population_total(counties: list[CountyDemographics]) -> int:
    all_counties_2014_pop = []
    for county in counties:
        pop_2014 = county.population["2014 Population"]
        all_counties_2014_pop.append(pop_2014)
    total_pop = sum(all_counties_2014_pop)
    return total_pop

# Part 2
# Purpose: take a list of object of class CountyDemographics and a specified state abbreviation, then returnn a list of county demographics objects that are in the state
# Input: list of objects of class CountyDemographics and a state (string)
# Output: list of objects of class CountyDemographics
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    in_state = []
    for county in counties:
        if county.state == state:
            in_state.append(county)
    return in_state

# Part 3
def population_by_education(counties: list[CountyDemographics], ed_level: str) -> float:
    # Purpose: take a list of counties and return the total 2014 population that has a given level of education
    # Input: list of objects of class CountyDemographics and a string
    # Output: float
    try:
        pop_2014_with_ed_level = []
        for county in counties:
            pop_2014_with_ed_level.append(county.education[ed_level] * (county.population["2014 Population"] / 100))
        total = sum(pop_2014_with_ed_level)
        return total
    except KeyError:
        print("KeyError: specified key does not exist.")
        return 0

def population_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    # Purpose: take a list of counties and return the total 2014 population that is the given ethnicity
    # Input: list of objects of class CountyDemographics and a string
    # Output: float
    try:
        pop_2014_ethnicity = []
        for county in counties:
            pop_2014_ethnicity.append(county.ethnicities[ethnicity] * (county.population["2014 Population"] / 100))
        total = sum(pop_2014_ethnicity)
        return total
    except KeyError:
        print("KeyError: specified key does not exist.")
        return 0

def population_below_poverty_level(counties: list[CountyDemographics], pov_level: str) -> float:
# Purpose: take a list of counties and return the total 2014 population that is below the poverty line
# Input: list of objects of class CountyDemographics and a string
# Output: float
    try:
        pop_2014_in_pov = []
        for county in counties:
            pop_2014_in_pov.append(county.income[pov_level] * (county.population["2014 Population"] / 100))
        total = sum(pop_2014_in_pov)
        return total
    except KeyError:
        print("KeyError: specified key does not exist.")
        return 0

# Part 4
def percent_by_education(counties: list[CountyDemographics], ed_level: str) -> float:
# Purpose: given a list of counties, return the proportion of 2014 population with a given education level
# Input: list of objects of class CountyDemographics
# Output: float
    pop_2014 = population_total(counties)
    ed_level_pop = population_by_education(counties, ed_level)
    ed_level_prop = ed_level_pop / pop_2014
    return ed_level_prop

def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
# Purpose: given a list of counties, return the proportion of 2014 population with a given ethnicity
# Input: list of objects of class CountyDemographics
# Output: float
    pop_2014 = population_total(counties)
    ethnicity_pop = population_by_ethnicity(counties, ethnicity)
    ethnicity_prop = ethnicity_pop / pop_2014
    return ethnicity_prop

def percent_below_poverty_level(counties: list[CountyDemographics], pov_level: str) -> float:
# Purpose: given a list of counties, return the proportion of 2014 population below the poverty line
# Input: list of objects of class CountyDemographics
# Output: float
    pop_2014 = population_total(counties)
    pop_in_pov = population_below_poverty_level(counties, pov_level)
    poverty_prop = (pop_in_pov / pop_2014)
    return poverty_prop

# Part 5
def education_greater_than(counties: list[CountyDemographics], ed_level: str, threshold: float) -> list[CountyDemographics]:
    # Purpose: given a list of counties and an education level, return list of counties with percent with that education greater than threshold value given
    # Input: list of objects of class CountyDemographics, education level (string), threshold value (float)
    # Output: list of objects of class CountyDemographics
    ed_greater_than = []
    for county in counties:
        if county.education[ed_level] > threshold:
            ed_greater_than.append(county)
    return ed_greater_than

def education_less_than(counties: list[CountyDemographics], ed_level: str, threshold: float) -> list[CountyDemographics]:
    # Purpose: given a list of counties and an education level, return list of counties with percent with that education less than threshold value given
    # Input: list of objects of class CountyDemographics, education level (string), threshold value (float)
    # Output: list of objects of class CountyDemographics
    ed_less_than = []
    for county in counties:
        if county.education[ed_level] < threshold:
            ed_less_than.append(county)
    return ed_less_than

def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity: str, threshold: float) -> list[CountyDemographics]:
    # Purpose: given a list of counties and an ethnicity, return list of counties with percent with percentages of that ethnicity that are greater than threshold value given
    # Input: list of objects of class CountyDemographics, ethnicity (string), threshold value (float)
    # Output: list of objects of class CountyDemographics
    ethnicity_greater_than = []
    for county in counties:
        if county.ethnicities[ethnicity] > threshold:
            ethnicity_greater_than.append(county)
    return ethnicity_greater_than

def ethnicity_less_than(counties: list[CountyDemographics], ethnicity: str, threshold: float) -> list[CountyDemographics]:
    # Purpose: given a list of counties and an ethnicity, return list of counties with percent with percentages of that ethnicity that are less than threshold value given
    # Input: list of objects of class CountyDemographics, ethnicity (string), threshold value (float)
    # Output: list of objects of class CountyDemographics
    ethnicity_less_than = []
    for county in counties:
        if county.ethnicities[ethnicity] < threshold:
            ethnicity_less_than.append(county)
    return ethnicity_less_than

def below_poverty_greater_than(counties: list[CountyDemographics], pov_level: str, threshold: float) -> list[CountyDemographics]:
    # Purpose: given a list of counties and an ethnicity, return list of counties with percent with percentages below poverty line that are greater than threshold value given
    # Input: list of objects of class CountyDemographics, poverty level (string), threshold value (float)
    # Output: list of objects of class CountyDemographics
    pov_level_greater_than = []
    for county in counties:
        if county.income[pov_level] > threshold:
            pov_level_greater_than.append(county)
    return pov_level_greater_than

def below_poverty_less_than(counties: list[CountyDemographics], pov_level: str, threshold: float) -> list[CountyDemographics]:
    # Purpose: given a list of counties and an ethnicity, return list of counties with percent with percentages below poverty line that are less than threshold value given
    # Input: list of objects of class CountyDemographics, poverty level (string), threshold value (float)
    # Output: list of objects of class CountyDemographics
    pov_level_less_than = []
    for county in counties:
        if county.income[pov_level] < threshold:
            pov_level_less_than.append(county)
    return pov_level_less_than
