"""Unit tests for main module."""
import pytest
from travelagent.main import run, _get_default_inputs


class TestMainInputs:
    """Tests for input handling."""

    def test_default_inputs_complete(self):
        inputs = _get_default_inputs()
        required = ["origin", "destination", "start_date", "end_date", "travelers", "budget"]
        for key in required:
            assert key in inputs
            assert inputs[key]

    def test_run_missing_inputs_raises(self):
        with pytest.raises(ValueError, match="Missing required inputs"):
            run({"origin": "Dallas"})

    def test_run_empty_inputs_raises(self):
        with pytest.raises(ValueError, match="Missing required inputs"):
            run({"origin": "", "destination": "", "start_date": "", "end_date": "", "travelers": "", "budget": ""})
