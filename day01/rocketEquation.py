import math

answer = 0
masses = []

def get_required_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    print("Mass:", mass)
    print("Fuel:", fuel)
    return fuel + get_required_fuel(fuel)

with open('input.txt', 'r') as f:
    lines = f.readlines()
    masses = [int(line) for line in lines]

for mass in masses:
    fuel = get_required_fuel(mass)
    answer += fuel

print("Answer:", answer)
