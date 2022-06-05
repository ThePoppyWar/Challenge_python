class Ingredients:
    def __init__(self, name: str, amount_protein_100g: float or int, amount_carbohydrates_100g: float or int, amount_fat_100g: float or int):
        self.name = name
        self.protein = amount_protein_100g
        self.carbohydrates = amount_carbohydrates_100g
        self.fat = amount_fat_100g



class Meal:
    def __init__(self, name_meal: str):
        self.name = name_meal
        self.intgredients = list()

    def add_ingredients_meal(self, ingredient, grams: int):
        self.intgredients.append([ingredient, grams])

    def print(self):
        print(f'Posiłek: {self.name}')
        protein_sum = 0
        carb_sum = 0
        fat_sum = 0
        kcal_sum = 0
        for ingredient in self.intgredients:
            protein = ingredient[1] / 100 * ingredient[0].protein
            carbohydrates = ingredient[1] / 100 * ingredient[0].carbohydrates
            fat = ingredient[1] / 100 * ingredient[0].fat
            kcal = protein * 4 + carbohydrates * 4 + fat * 9.4

            protein_sum +=protein
            carb_sum += carbohydrates
            fat_sum += fat
            kcal_sum += kcal

            print(f'- {ingredient[1]}g {ingredient[0].name}'
                  f'- ({protein}g białka, {carbohydrates}g węglowodanów, {fat}g tłuszczy, {kcal} kcal)')
            print(f'Razem: {protein_sum}g białka, {carb_sum}g węglowodanów, {fat_sum}g tłuszczy, {kcal_sum} kcal')
            print()
            return protein_sum, carb_sum, fat_sum, kcal_sum



class Plan_of_meal:
    def __init__(self, name_plan_of_meal: str):
        self.name_plan_of_meal = name_plan_of_meal
        self.plan_meal = list()

    def add_meal(self, meal_name: Meal):
        self.plan_meal.append(meal_name)

    def print(self):
        print(self.name_plan_of_meal)
        day_nutritional_values = [0, 0, 0, 0]
        for meal in self.plan_meal:
            meal_nutritional_values = meal.print()
            j = 0
            for i in meal_nutritional_values:
                day_nutritional_values[j] += i
                j +=1
        print(f'RAZEM: {day_nutritional_values[0]}g białka, {day_nutritional_values[1]}g węglowodanów,'
              f'{day_nutritional_values[2]}g tłuszczy, {day_nutritional_values[3]} kcal')




def main():
    egg = Ingredients('Jajko', 13, 1.1, 11)
    tomato = Ingredients('Pomidor', 0.9, 3.9, 0.2)
    bread = Ingredients('Chleb', 9, 49, 3.2)

    scrambled_eggs = Meal('Jajecznica')
    scrambled_eggs.add_ingredients_meal(egg, 200)
    scrambled_eggs.add_ingredients_meal(tomato, 50)

    sandwich = Meal('Kanapka')
    sandwich.add_ingredients_meal(bread, 25)
    sandwich.add_ingredients_meal(tomato, 50)

    menu_basic = Plan_of_meal("Oszczędny")
    menu_basic.add_meal(scrambled_eggs)
    menu_basic.add_meal(sandwich)

    menu_basic.print()

if __name__ == '__main__':
    main()
