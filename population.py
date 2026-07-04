# POPULATION SIMULATOR USING BASIC VARIABLES AND FUNCTIONS

# Important things
import random # library for random number generation
import matplotlib.pyplot as plt # library for plotting graphs


# Defining all our variables
population = 1000
iq = 95
food = 67
economy = 67

year = 0
child_survival = 0
mortality = 0.01


# I've added Matplotlib to make graphs, so we define some lists to store the history of the variables
history_population = []
history_iq = []
history_food = []
history_economy = []


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


    # Finally with the IQ (recent modification)
    if iq < 80:
        children -= 0.5
    
    elif iq < 85:
        children -= 0.2


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


# You can change the number of years to simulate
while True:
    option = input("Do you want to simulate (1), see statistics (2), exit (3) or see graphs (4)? ")

    if option == "1":
        years = int(input("How many years do you want to simulate this population? "))

        for i in range(years):
            # First we add the append, which saves the data from each year
            history_population.append(population)
            history_iq.append(iq)
            history_food.append(food)
            history_economy.append(economy)
            
            
            # Then we calculate the new values for the next year (some are random)
            children, child_survival, mortality, iq = birth_rate(food, economy, iq)
            population = int(population + (population / 2 * (children / 25) * child_survival) - mortality) # formula get by AI

            food = food + random.randint(-3, 3)
            economy = economy + random.randint(-3, 3)


            # We need limits for not having negative values
            economy = max(5, min(100, economy))
            food = max(5, min(100, food))
            iq = max(70, min(130, iq))

            year += 1


            # We can't have negative population too
            if population <= 0:
                print(f"Everyone died in year {year}.")
                break

        print(f"Simulated {years} years.\n")

    elif option == "2":
        print(f"Currently simulated {year} years.")
        print(f"- Current Population: {population}")
        print(f"- Current IQ: {int(iq)}")
        print(f"- Current Food Supply: {food}")
        print(f"- Current Economy: {economy}\n")

    elif option == "3":
        print("Exiting the simulation.")
        break

    elif option == "4": # part done by AI, which will be learnt later (it's just testing the graphing capabilities)
        plt.figure(figsize=(10, 6))
        plt.plot(history_population, label="Population")
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.title("Population over time")
        plt.legend()
        plt.show()

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.\n")

    if population > 1000000000: # if not it bugges
        print("Population has exceeded 1,000,000,000. Ending simulation.")
        break