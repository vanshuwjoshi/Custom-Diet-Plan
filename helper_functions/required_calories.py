def get_required_calories(maintenance_calories, current_weight, desired_weight):
    if desired_weight > current_weight:
        maintenance_calories += 500
    elif desired_weight < current_weight:
        maintenance_calories -= 500
    else:
        return maintenance_calories
    return maintenance_calories
