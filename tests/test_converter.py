"""Tests for the core converter module."""

import pytest

from temperature_converter.converter import (
    ABSOLUTE_ZERO_F,
    MAX_TEMPERATURE_F,
    fahrenheit_to_celsius,
)


# ── Happy-path conversions ────────────────────────────────────────────


class TestFahrenheitToCelsius:
    """Verify correct conversions for well-known reference points."""

    def test_freezing_point(self) -> None:
        assert fahrenheit_to_celsius(32) == 0.0

    def test_boiling_point(self) -> None:
        assert fahrenheit_to_celsius(212) == 100.0

    def test_body_temperature(self) -> None:
        assert fahrenheit_to_celsius(98.6) == 37.0

    def test_absolute_zero(self) -> None:
        assert fahrenheit_to_celsius(-459.67) == -273.15

    def test_negative_forty_crossover(self) -> None:
        """−40 is the same in both scales."""
        assert fahrenheit_to_celsius(-40) == -40.0

    def test_zero_fahrenheit(self) -> None:
        assert fahrenheit_to_celsius(0) == -17.78

    def test_integer_input(self) -> None:
        result = fahrenheit_to_celsius(100)
        assert isinstance(result, float)
        assert result == 37.78

    def test_large_value(self) -> None:
        result = fahrenheit_to_celsius(1_000_000)
        assert isinstance(result, float)


# ── Type-safety ───────────────────────────────────────────────────────


class TestTypeValidation:
    """Ensure non-numeric types are rejected."""

    def test_string_rejected(self) -> None:
        with pytest.raises(TypeError, match="got str"):
            fahrenheit_to_celsius("100")  # type: ignore[arg-type]

    def test_none_rejected(self) -> None:
        with pytest.raises(TypeError, match="got NoneType"):
            fahrenheit_to_celsius(None)  # type: ignore[arg-type]

    def test_bool_rejected(self) -> None:
        with pytest.raises(TypeError, match="got bool"):
            fahrenheit_to_celsius(True)  # type: ignore[arg-type]

    def test_list_rejected(self) -> None:
        with pytest.raises(TypeError, match="got list"):
            fahrenheit_to_celsius([100])  # type: ignore[arg-type]


# ── Boundary / range validation ───────────────────────────────────────


class TestRangeValidation:
    """Ensure physically impossible values are rejected."""

    def test_below_absolute_zero(self) -> None:
        with pytest.raises(ValueError, match="below absolute zero"):
            fahrenheit_to_celsius(ABSOLUTE_ZERO_F - 1)

    def test_above_maximum(self) -> None:
        with pytest.raises(ValueError, match="exceeds maximum"):
            fahrenheit_to_celsius(MAX_TEMPERATURE_F + 1)

    def test_nan_rejected(self) -> None:
        with pytest.raises(ValueError, match="NaN"):
            fahrenheit_to_celsius(float("nan"))

    def test_positive_infinity_rejected(self) -> None:
        with pytest.raises(ValueError, match="infinity"):
            fahrenheit_to_celsius(float("inf"))

    def test_negative_infinity_rejected(self) -> None:
        with pytest.raises(ValueError, match="infinity"):
            fahrenheit_to_celsius(float("-inf"))
