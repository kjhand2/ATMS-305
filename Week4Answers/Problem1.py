fleet = 100
drivers = 30
passengers = 85

unused_cars = fleet - drivers

used_cars = fleet - unused_cars

total_capacity = used_cars * 4

avg_pass = passengers / used_cars

print(unused_cars, 'cars are not used today.')

print(used_cars, 'cars are used today.')

print('The total capacity of the fleet is ', total_capacity, '.')

print('The average number of passengers per car is', avg_pass, '.')

print('done with report')
