"""Tiny functions used by the Git Safety Belt Lab."""


def total_items(pretzels: int, raisins: int, chocolate: int) -> int:
    """Return the total number of trail-mix pieces."""
    return pretzels + raisins + chocolate


def servings_possible(total: int, serving_size: int) -> int:
    """Return the number of complete servings available."""
    if serving_size <= 0:
        raise ValueError("serving_size must be greater than zero")
    return total // serving_size


if __name__ == "__main__":
    pieces = total_items(12, 8, 10)
    print(f"Trail mix pieces: {pieces}")
    print(f"Complete servings of 5: {servings_possible(pieces, 5)}")
