from encontrar_vocal import saca_vocales
import pytest

@pytest.mark.parametrize(
    "cadena, esperado",
    [
        ("Hola me llamo mario", "oaeaoaio"),
        ("Hey", "e"),
        ("Bjhgtkv", ""),
        ("aeiouAEIOU", "aeiouAEIOU"),
        ("1", "")
    ]
)
def test_saca_vocales(cadena, esperado):
    assert saca_vocales(cadena) == esperado