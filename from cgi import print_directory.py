from cgi import print_directory
from ctypes.wintypes import MSG


x = 0
while x <= 5:
    print(x)
    x = x+1


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}    
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
    