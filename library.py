def miles_to_kilometers(miles: float) -> float:
    if miles < 0:
        raise ValueError("Miles cannot be negative.")
    kilometers = miles * 1.60934
    return kilometers


def get_unique_sorted_elements(data) -> tuple:
    unique_elements = sorted(set(data))
    return tuple(unique_elements)

