
# POPULATION SIMULATOR USING BASIC VARIABLES AND FUNCTIONS

# Important thing
import random # library for random number generation


# Defining all our variables
population = 1000
iq = 95
food = 67
economy = 67

year = 0
child_survival = 0
mortality = 0.01


# Defining the global function
def birth_rate(food, economy, iq):
    children = 3.5 - ((iq - 70) * 0.038)


    # First with food
    if food < 30:
        children += 0.5
        child_survival = 0.5

    elif food < 60:
        children += 0.1
        child_survival = 0.75

    elif food < 80:
        children += 0
        child_survival = 0.9

    elif food <= 100:
        children -= 0.2
        child_survival = 0.97


    # Then with economy
    if economy < 30:
        children += 0.4

    elif economy < 60:
        children += 0
    
    elif economy < 80:
        children -= 0.2

    elif economy <= 100:
        children -= 0.4

    
    # Extra things to consider for mortality based on economy    
    mortality = 0.01 * population

    if economy < 30:
        mortality += 0.005 * population

    elif economy > 70:
        mortality -= 0.003 * population
    
    else:
        mortality += 0.001 * population


    # Multivariable functions to determine IQ based on food and economy
    if food > 60 and economy > 50:
        iq += 0.3

    
    if food < 40 or economy < 30:
        iq -= 0.7


    # Finally, we need to return all the variables we have calculated
    return children, child_survival, mortality, iq


# We make an infinite loop to simulate
while year < 100:
    children, child_survival, mortality, iq = birth_rate(food, economy, iq)
    year += 1
    population = int(population + (population / 2 * (children / 25) * child_survival) - mortality)

    food = food + random.randint(-3, 3)
    economy = economy + random.randint(-3, 3)

    
    # We need limits for not having negative values
    economy = max(5, min(100, economy))
    food = max(5, min(100, food))
    iq = max(70,  min(130, iq))


    # We can't have negative population too
    if population <= 0:
        print(f"Everyone died in year {year}.")
        break

else:
    print("Simulation complete after 100 years.")
    print(f"- Final Population: {population}")
    print(f"- Final IQ: {int(iq)}")
    print(f"- Final Food Supply: {food}")
    print(f"- Final Economy: {economy}")