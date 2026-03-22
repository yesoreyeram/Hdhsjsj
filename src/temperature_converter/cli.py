"""Command-line interface for the temperature converter."""

import argparse
import sys

from temperature_converter.converter import fahrenheit_to_celsius


def main(argv: list[str] | None = None) -> int:
    """Entry point for the CLI.

    Args:
        argv: Command-line arguments (defaults to ``sys.argv[1:]``).

    Returns:
        Exit code: 0 on success, 1 on user error.
    """
    parser = argparse.ArgumentParser(
        description="Convert Fahrenheit to Celsius",
    )
    parser.add_argument(
        "fahrenheit",
        type=float,
        help="Temperature in degrees Fahrenheit",
    )
    args = parser.parse_args(argv)

    try:
        celsius = fahrenheit_to_celsius(args.fahrenheit)
    except (TypeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"{args.fahrenheit} °F = {celsius} °C")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
