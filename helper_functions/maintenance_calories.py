def get_maintenance_calories(bmr, activity_level):
    if activity_level == "Sedentary":
        bmr *= 1.2
    elif activity_level == "Moderately active":
        bmr *= 1.375
    elif activity_level == "Highly active":
        bmr *= 1.725
    else:
        bmr *= 1.9
    return bmr