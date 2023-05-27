def miles_to_kilometers(miles: int|float) -> int|float:
    if miles < 0:
        raise ValueError("Miles cannot be negative.")
    return miles * 1.60934


def get_unique_sorted_elements(data) -> tuple:
    unique_elements = sorted(set(data))
    return tuple(unique_elements)

