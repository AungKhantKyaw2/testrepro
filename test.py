# import math

# price =10.99

# print(f" The price is ${price} cm")

# a = 3.5
# a= round(a)
# print(a)



# # radius = float(input("Enter the radius of  a circle"))

# # area =math.pi  * pow(radius,2)


# # print(f"The area of circle is   {area}cm2")

# # help(int)

# # a.bit_count()

# nums = [1, 2, 3, 4, 5]
# print(nums[0:4])

# import time

# a  =  int(input("Enter the time seconds "))


# for x in range(a,-2,-1):
#     print(x)


# fruits = [1,2,2,3,4,5]

# for fruit in range(0,len(fruits)):
#     print(fruit)


# foods = {
#       "chips":1.50,
#       "potatoes":1.50

# }


# print(dir(foods))

# # print(foods.items())

# a =foods.items()

# print(a[0])


menu = {
    "pizza" : 3.00  ,
    "nachos" :4.50,
    "popcorn":6.00,
    "fries":2.50,
    "chips":1.00,
    "pretzel":3.50,
    "soda":3.00,
    "lemonade":4.25
}

cart=[]

total = 0


print("------Menu-------")
for key,value in menu.items():
    print(f"{key:10} : {value:.2f}")

print("------------------")

while True:
    food = input("Select an item (q to quit):").lower()

    if food == "q":
        break
    elif food in menu:
        
        cart.append(food)



for food in cart:

    total += menu.get(food)

    print(end=f'{food:10} - ')
    print(menu.get(food))


print(f"Total price is {total:.2f}")



