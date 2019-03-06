#calories from fats and carbohydrates


def calories_from_fat(fat):
    calories_fat = fat * 9
    return calories_fat


def calories_from_carb(carbs):
    calories_carb = carbs * 4
    return calories_carb


def main():
    fat = float(input('Enter the fat intake for the day: '))
    carbs = float(input('Enter the carbohydrate intake for the day: '))
    total_calories = calories_from_fat(fat) + calories_from_carb(carbs)
    print('The total calorie intake for the day is:',format(total_calories,'.2f'))


if __name__ == '__main__':
    main()