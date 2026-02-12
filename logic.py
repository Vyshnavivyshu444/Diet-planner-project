import pandas as pd
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FOODS_CSV = os.path.join(BASE_DIR,  "foods.csv")
WORKOUT_CSV = os.path.join(BASE_DIR,  "workout.csv")

foods_df = pd.read_csv(FOODS_CSV)
workouts_df = pd.read_csv(WORKOUT_CSV)

foods_df.columns = foods_df.columns.str.strip().str.lower()
workouts_df.columns = workouts_df.columns.str.strip().str.lower()

def generate_plan(age, gender, height, weight, goal, diet):

    if not gender or gender == "undefined":
        gender = "Not specified"

    filtered_foods = foods_df[foods_df['diet'].str.lower() == diet.lower()]
    filtered_workouts = workouts_df[workouts_df['goal'].str.lower() == goal.lower()]

    if filtered_foods.empty:
        raise Exception("No foods found for selected diet")

    if filtered_workouts.empty:
        raise Exception("No workouts found for selected goal")

    meals = random.sample(
        filtered_foods['food'].astype(str).tolist(),
        min(3, len(filtered_foods))
    )

    workouts = random.sample(
        filtered_workouts['workout'].astype(str).tolist(),
        min(3, len(filtered_workouts))
    )

    # Take ONE calorie value (not repeating)
    meal_calories = int(filtered_foods['calories'].iloc[0])
    workout_calories = int(filtered_workouts['calories_burn'].iloc[0])

    return {
        "gender": gender,
        "meal_calories": meal_calories,
        "workout_calories": workout_calories,
        "meals": meals,          # ✅ ARRAY
        "workouts": workouts     # ✅ ARRAY
    }


