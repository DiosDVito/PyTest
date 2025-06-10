import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from areas import area_triangulo

def test_area_triangulo_base5_altura7():
    """Validar el resultado cuando la base sea 5 y la altura sea 7."""
    base = 5
    altura = 7
    area_esperada = 17.5  # (5 * 7) / 2
    
    area_calculada = area_triangulo(base, altura)
    
    assert area_calculada == area_esperada

def test_area_triangulo_valores_negativos():
    """Validar que no se acepten valores negativos para la base ni para la altura."""
    with pytest.raises(ValueError) as excinfo:
        area_triangulo(-5, 7)
    assert "La base no puede ser un valor negativo" in str(excinfo.value)
    
    
    with pytest.raises(ValueError) as excinfo:
        area_triangulo(5, -7)
    assert "La altura no puede ser un valor negativo" in str(excinfo.value)

def test_area_triangulo_base_cero():
    """Validar que la base no sea cero."""
    with pytest.raises(ValueError) as excinfo:
        area_triangulo(0, 7)
    assert "La base no puede ser cero" in str(excinfo.value)
