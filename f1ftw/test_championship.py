import objects
from calculate_drivers_championship import CalculateDriversChampionship

championship = CalculateDriversChampionship("Russian")
print("\nRNK\tPTS\tDRIVER\n")
for championship_driver in championship:
    print(str(championship_driver.ranking) + "\t" + str(championship_driver.points) + "\t" + str(championship_driver.driver.person_name))
