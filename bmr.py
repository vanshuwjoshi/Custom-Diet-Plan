def get_bmr(weight, height, age, gender):
    bmr = (10 * weight) + (6.25 * height) - (5 * age)
    if gender == "Male":
        bmr = bmr + 5
    else:
        bmr = bmr - 161
    return bmr
