from datetime import date, timedelta
from seasons import MyDate
import pytest

def test_valid():
    assert MyDate.diff_from_today((date.today() - timedelta(days=365)).isoformat()) == 525600
    assert MyDate.diff_from_today((date.today() - timedelta(days=1)).isoformat()) == 1440

def test_str():
    assert MyDate.in_str(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert MyDate.in_str(1440) == "One thousand, four hundred forty minutes"

def test_invalid_date():
    print("Hello")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        MyDate.diff_from_today("cat")
    print(pytest_wrapped_e)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "Invalid date"