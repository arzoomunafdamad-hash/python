name = "Pizza"
price = 12
weight = 12
is_vegetarian = True
print("snack type:", name)
print("cost:", price)
print("mass:", weight)
print("kind of snack:", is_vegetarian)
print(type(name))
print(type(price))
print(type(weight))
print(type(is_vegetarian))
total_cost = price * weight
print("total cost:", total_cost)
check = weight < price
print("is weight greater:", check)
is_weight = weight == price
print("is weight equal to the price:", is_weight)
snackname = name + " is a delicious snack"
print("concadination of strings:", snackname)
print("lenght of a string:", len(name))
print("extract first element from string:", name[0])
print("extract last element from string:", name[-1])
print("reverse the string:", name[-1::-1])

price_a = 10
price_b = 20
print("before", price_a, price_b)
Temp = price_a
price_a = price_b
price_b = Temp
print("after", price_a, price_b)