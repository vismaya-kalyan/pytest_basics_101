import pytest
from calculator import Calculator, CalculatorError


class TestAdd:
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(2, 3)
        assert result == 5

    def test_add_raise(self):
        calculator = Calculator()
        with pytest.raises(CalculatorError) as context:
            result = calculator.add("abc", "d")
        # (str(context.value))

    @pytest.mark.parametrize(
        "a, b, expected", [(1, 1, 2), (2, 1, 3), (3, 1, 4), (4, 1, 5)]
    )
    def test_add_param(self, a, b, expected):
        calculator = Calculator()
        result = calculator.add(a, b)
        assert result == expected


class TestSubtract:
    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(2, 3)
        assert result == -1


class TestMultiply:
    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(2, 3)
        assert result == 6


class TestDivide:
    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(9, 3)
        assert result == 3

    def test_divide_by_zero(self):
        calculator = Calculator()
        with pytest.raises(CalculatorError) as context:
            result = calculator.divide(9, 0)


class TestFixture:
    def test_fixture(self, my_fixture):
        assert my_fixture == 42

    def test_capsys(self, capsys):
        print("Hello")
        out, err = capsys.readouterr()
        assert "Hello\n" == out

    def test_monkeypatch(self, monkeypatch):
        def fake_add(a, b):
            return 42

        calculator = Calculator()
        monkeypatch.setattr(calculator, "add", fake_add)
        assert calculator.add(2, 3) == 42

    def test_tempdir(self, tmpdir):
        some_file = tmpdir.join("something.txt")
        some_file.write('{"hello":"world"}')

        calculator = Calculator()
        result = calculator.read_json(str(some_file))
        assert result["hello"] == "world"
