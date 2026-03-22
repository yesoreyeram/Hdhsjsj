"""Tests for the CLI entry point."""

import pytest

from temperature_converter.cli import main


class TestCLI:
    """Verify CLI output and exit codes."""

    def test_successful_conversion(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main(["212"])
        assert exit_code == 0
        assert "100.0 °C" in capsys.readouterr().out

    def test_freezing_point(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main(["32"])
        assert exit_code == 0
        assert "0.0 °C" in capsys.readouterr().out

    def test_invalid_range(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main(["-999"])
        assert exit_code == 1
        assert "below absolute zero" in capsys.readouterr().err

    def test_missing_argument(self) -> None:
        with pytest.raises(SystemExit):
            main([])
