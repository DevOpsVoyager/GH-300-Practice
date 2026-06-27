import importlib.util
from pathlib import Path


module_path = Path(__file__).resolve().parents[1] / "src" / "app.py"
spec = importlib.util.spec_from_file_location("app_module", module_path)
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)


def test_prime_numbers():
    assert app_module.is_prime(2) is True
    assert app_module.is_prime(3) is True
    assert app_module.is_prime(17) is True


def test_non_prime_numbers():
    assert app_module.is_prime(1) is False
    assert app_module.is_prime(4) is False
    assert app_module.is_prime(49) is False
    assert app_module.is_prime(-3) is False
