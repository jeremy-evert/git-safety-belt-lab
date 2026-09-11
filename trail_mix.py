"""Tiny functions used by the Git Safety Belt Lab."""


def total_items(pretzels: int, raisins: int, chocolate: int) -> int:
    """Return the total number of trail-mix pieces."""
    return pretzels + raisins + chocolate


def servings_possible(total: int, serving_size: int) -> int:
    """Return the number of complete servings available."""
    if serving_size <= 0:
        raise ValueError("serving_size must be greater than zero")
    return total // serving_size


def average_pieces_per_category(pretzels: int, raisins: int, chocolate: int) -> float:
    """Return the arithmetic mean of the three values as a float."""
    return (pretzels + raisins + chocolate) / 3.0


if __name__ == "__main__":
    pieces = total_items(12, 8, 10)
    servings = servings_possible(pieces, 5)
    print(f"Complete servings of 5: {servings}")
