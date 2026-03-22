"""Core conversion logic with strict input validation."""

# Absolute zero in Fahrenheit. No physical temperature can be below this.
ABSOLUTE_ZERO_F = -459.67

# Upper bound: estimated temperature of the hottest known star (~200,000 °F).
# Provides a sane upper limit to reject nonsensical inputs.
MAX_TEMPERATURE_F = 1_000_000_000.0


def fahrenheit_to_celsius(value: float) -> float:
    """Convert a Fahrenheit temperature to Celsius.

    Args:
        value: Temperature in degrees Fahrenheit.  Must be a finite
            number no lower than absolute zero (-459.67 °F) and no
            higher than ``MAX_TEMPERATURE_F``.

    Returns:
        The equivalent temperature in degrees Celsius, rounded to
        two decimal places.

    Raises:
        TypeError: If *value* is not ``int`` or ``float``.
        ValueError: If *value* is NaN, infinite, or outside the
            physically valid range.
    """
    _validate(value)
    celsius = (value - 32) * 5.0 / 9.0
    return round(celsius, 2)


def _validate(value: object) -> None:
    """Validate that *value* is a finite number in a sensible range."""
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"Temperature must be int or float, got {type(value).__name__}"
        )

    # Reject bool (subclass of int) to avoid silent misuse.
    if isinstance(value, bool):
        raise TypeError("Temperature must be int or float, got bool")

    # Must be finite.
    if value != value:  # NaN check without importing math
        raise ValueError("Temperature must be a finite number, got NaN")

    if value == float("inf") or value == float("-inf"):
        raise ValueError("Temperature must be a finite number, got infinity")

    if value < ABSOLUTE_ZERO_F:
        raise ValueError(
            f"Temperature {value} °F is below absolute zero ({ABSOLUTE_ZERO_F} °F)"
        )

    if value > MAX_TEMPERATURE_F:
        raise ValueError(
            f"Temperature {value} °F exceeds maximum allowed ({MAX_TEMPERATURE_F} °F)"
        )
