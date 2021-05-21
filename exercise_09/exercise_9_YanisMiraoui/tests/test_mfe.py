import sys
import os
import pytest

scriptsdir = os.path.join(os.path.dirname(__file__), "..", "scripts")
sys.path.append(scriptsdir)


def test_mfe_length():
    with open(os.path.join(scriptsdir, "tests_report_mfe.py"), "r") as f:
        assert (
            len(f.readlines()) == 2
        ), "Expected at most two lines in tests_report_mfe.py"


def test_mfe_raises_same_error():
    with pytest.raises(ValueError) as e:
        import tests_report_mfe
    assert e.value.args[0] == "unconverted data remains: +08:00"
