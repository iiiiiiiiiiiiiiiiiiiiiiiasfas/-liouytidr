# finance_utils.py

def round_to_nearest(value, nearest):

    if nearest == 0:
        raise ValueError("Значение 'nearest' не может быть равно нулю.")

    rounded_value = round(value / nearest) * nearest
    return rounded_value
