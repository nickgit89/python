favorite_foods = ["pizza", "hamburgers", "pepperoni", "chipotle"]

best_foods = favorite_foods[:]

print(best_foods)

cool_foods = best_foods

favorite_foods.append("french fries")

favorite_foods.append("gelato")

favorite_foods.remove("hamburgers")

favorite_foods.insert(2, "stir fry")

print(f"Best foods list: {best_foods}")
print(f"Favorite Foods: {favorite_foods}")
print(f"cool foods: {cool_foods}") 



