pasta = ("Spaghetti", "Italian", 25, "Medium")
biryani = ("Biryani", "Indian", 40, "Hard")
print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])

all_recipes = (pasta, biryani)
print("\nFirst Recipe Name:", all_recipes[0][0])
print("Second Recipe Time:", all_recipes[1][2],"minutes")
print("Pasta details (sliced):", pasta[1:3])

print("\nPasta Recipe Details:")
for detail in pasta:
    print(" -", detail)


pasta_ingredients = {"Pasta", "Tomato Sauce", "Parmesan Cheese", "Olive Oil", "Garlic", "Salt"}
biryani_ingredients = {"Basmati Rice", "Chicken", "Yogurt", "Onions", "Garlic", "Ginger", "Spices", "Saffron", "Cilantro"}
print("\nPasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)
print("Total Ingredients in Pasta:", len(pasta_ingredients))
print("Total Ingredients in Biryani:", len(biryani_ingredients))
pasta_ingredients.add("Pepper")
pasta_ingredients.add("Basil")
pasta_ingredients.remove("Salt")
print("\nUpdated Pasta Ingredients:", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common_ingredients = pasta_ingredients.intersection(biryani_ingredients)
only_pasta_ingredients = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll Ingredients(union):", all_ingredients)
print("Common Ingredients(intersection):", common_ingredients)
print("Ingredients only in Pasta(difference):", only_pasta_ingredients)
print("Not shared(symmetric difference):", unique_to_each)






s1={"blue","yellow","Red"}

s2={"black","Orange","blue"}

s=s1.union(s2)

print("union ",s)

s=s1.intersection(s2)

print("intersection ",s)

s=s1.difference(s2)

print("difference ",s)

s=s1.symmetric_difference(s2)

print("symmetric_difference ",s)