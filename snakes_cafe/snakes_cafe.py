string = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************


Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
If you want to quit just type quit and notice that orders are case sensitive !
'''

print(string)

c_wings = 0
c_cookies = 0
c_Spring_Rolls = 0
c_Salmon = 0
c_Steak = 0
c_Meat_Tornado = 0
c_A_Literal_Garden = 0
c_Ice_Cream = 0
c_Cake=0
c_Pie = 0
c_Coffee = 0 
c_Tea = 0
c_Unicorn_Tears = 0

while True:
    i=input(">")
   
    if i == "Wings":
        c_wings += 1
        print(f"** {c_wings} order of {i} has been added to your meal **")
    elif i == "Cookies":
        c_cookies += 1
        print(f"** {c_cookies} order of {i} has been added to your meal **")
    elif i == "Spring Rolls":
        c_Spring_Rolls += 1
        print(f"** {c_Spring_Rolls} order of {i} has been added to your meal **")
    elif i == "Salmon":
        c_Salmon += 1
        print(f"** {c_Salmon} order of {i} has been added to your meal **")
    elif i == "Steak":
        c_Steak += 1
        print(f"** {c_Steak} order of {i} has been added to your meal **")
    elif i == "Meat Tornado":
        c_Meat_Tornado += 1
        print(f"** {c_Meat_Tornado} order of {i} has been added to your meal **")
    elif i == "A Literal Garden":
        c_A_Literal_Garden += 1
        print(f"** {c_A_Literal_Garden} order of {i} has been added to your meal **")
    elif i == "Ice Cream":
        c_Ice_Cream += 1
        print(f"** {c_Ice_Cream} order of {i} has been added to your meal **")
    elif i == "Cake":
        c_Cake += 1
        print(f"** {c_Cake} order of {i} has been added to your meal **")
    elif i == "Pie":
        c_Pie += 1
        print(f"** {c_Pie} order of {i} has been added to your meal **")
    elif i == "Coffee":
        c_Coffee += 1
        print(f"** {c_Coffee} order of {i} has been added to your meal **")
    elif i == "Tea":
        c_Tea += 1
        print(f"** {c_Tea} order of {i} has been added to your meal **")
    elif i == "Unicorn Tears":
        c_Unicorn_Tears += 1
        print(f"** {c_Unicorn_Tears} order of {i} has been added to your meal **")
    elif i == "quit":
        break
    else :
       print("Sorry, this order is not available on the menu")



