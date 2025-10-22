from src.nochevieja import transforma_hora
import pytest

@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("20:00"),
        ("15:30"),
        ("22:00"),
        ("11:15 ")
    ]
)

def test_mostrar_resultado(entrada, esperado):
    assert transforma_hora(entrada) == esperado