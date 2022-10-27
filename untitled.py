#Python program to display calendar

import calendar 
from termcolor import colored
f = ("""     
       🅗🅐🅟🅟🅨  🅝🅔🅦     🅨🅔🅐🅡
       
         𝐜𝐚𝐥𝐞𝐧𝐝𝐚𝐫 𝟐𝟎𝟐𝟑

""")

print ( colored(f,"red") )












year = 2023
month = 1

print( calendar.month(year, month  )) 

year = 2023
month = 2

print(      calendar.month(year, month )) 

year = 2023
month = 3

print(     calendar.month(year, month )) 
year = 2023
month = 4

print(     calendar.month(year, month )) 

year = 2023
month = 5

print(      calendar.month(year, month )) 

year = 2023
month = 6

print(     calendar.month(year,month ))

year = 2023
month = 7
print(calendar.month(year,month))

year = 2023
month = 8

print(calendar.month(year, month )) 

year = 2023
month = 9

print(calendar.month(year, month )) 

year = 2023
month = 10

print(calendar.month(year, month )) 
year = 2023
month = 11

print(calendar.month(year, month )) 

year = 2023
month = 12
print(calendar.month(year,month))
