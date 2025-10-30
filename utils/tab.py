def get_km(distance_km):
    if distance_km <= 1:
        return 1.50
    elif distance_km <= 3:
        return 2
    elif distance_km <= 7:
        return 3
    elif distance_km <= 10:
        return 4
    elif distance_km <= 12:
        return 5
    elif distance_km <= 16:
        return 6
    else:
        km_extra = distance_km - 16
        return round(6.00 + km_extra * 0.40, 2)
