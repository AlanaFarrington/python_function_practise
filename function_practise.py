# Write code for a simple travel app 
# Tripcademy (our trusty travel app) needs to allow passengers to plan a trip (duh).
# Write a function called trip_planner() that will have three parameters: first destination, second destination and final destination
# set final destination as a default argument of Codecademy HQ
# Write your code below:
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

# test your function by giving a selection of countries as arguments (some positional and some keyword)
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")
trip_planner("Brooklyn", "Queens")

# exploring variable scope
# Our users want to be able to save a list of their favorite places in our travel application.
favourite_locations = ["Paris", "Norway", "Iceland"]
count_locations = 0
def print_count_locations():
  count_locations = len(favourite_locations)
  print("There are " + str(count_locations) + "locations")
    
# This function will print the favorite locations
def show_favourite_locations():
  print("Your favorite locations are: " + favourite_locations[0] + ", " + favourite_locations[1] + " and " + favourite_locations[2])

print_count_locations()
show_favourite_locations()

#Our travel application is getting really popular. 
# Some of our users have posted on social media that it would be useful if our application could help them track their budget during trips. 
# We want to help them track their starting budget and let them know how much they have left after an expense.
current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: £" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
  return budget - expense
shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
print_remaining_budget(new_budget_after_shirt)

# use built in functions max(), min() and round() to find maximum, minimum and rounded prices (rounded to 1dp)
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)
rounded_price = round(tshirt_price, 1)
print(rounded_price)

# Our users liked the previous functionality that we added to our travel application, 
# but recently we have had an influx of users planning trips in Italy. 
# We want to create a small function to output the top places to visit in Italy. 
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)

# example trip planner
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)
trip_planner_welcome("Alana")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(3.5)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("UK", "Japan", estimate, "aeroplane")