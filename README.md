# Cálculo de Área de Triángulo

Este proyecto implementa una función para calcular el área de un triángulo y automatiza pruebas utilizando pytest y GitHub Actions.

## Requisitos

- Python 3.x
- pytest

## Estructura del proyecto

```
.
├── areas.py                  # Módulo con la función para calcular el área del triángulo
├── tests/                    # Directorio de pruebas
│   └── test_area_triangulo.py  # Pruebas para la función de área del triángulo
├── .github/                  # Configuración de GitHub Actions
│   └── workflows/            
│       └── python-tests.yml  # Workflow para automatizar las pruebas
└── README.md                 # Este archivo
```

## Funcionalidad

La función `area_triangulo(base, altura)` implementa el cálculo del área de un triángulo y valida:

- Que la base no sea cero
- Que ni la base ni la altura sean valores negativos

## Pruebas

Las pruebas automatizadas validan:

1. Prueba 1: Validar el resultado cuando la base sea 5 y la altura sea 7 (resultado esperado: 17.5)
2. Prueba 2: Validar que no se acepten valores negativos para la base ni para la altura
3. Prueba 3: Validar que la base no sea cero

### Ejecutar pruebas localmente

```bash
# Desde la raíz del proyecto
pytest tests/
```

## GitHub Actions

El proyecto está configurado con GitHub Actions para ejecutar automáticamente las pruebas cuando:

- Se hace push a las ramas main o master
- Se crea un pull request a las ramas main o master
- Se ejecuta manualmente el workflow desde la interfaz de GitHub

El archivo de configuración se encuentra en `.github/workflows/python-tests.yml`. 