import requests
import os

def fetch_meal_plan():
    api_key = os.getenv("SPOONACULAR_API_KEY")
    response = requests.get(f"https://api.spoonacular.com/mealplanner/generate?apiKey={api_key}&timeFrame=day")
    return response.json()

def get_meal_tool():
    def _tool(_):
        meals = fetch_meal_plan()
        return "\n".join([f"{meal['title']} - {meal['readyInMinutes']} mins" for meal in meals["meals"]])
    return _tool

def get_workout_tool():
    def _tool(_):
        return "Workout Suggestion: 3 sets of squats, push-ups, and planks. Add light cardio like jogging or jumping jacks."
    return _tool
