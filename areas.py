def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.
    
    Args:
        base: La base del triángulo
        altura: La altura del triángulo
        
    Returns:
        float: El área del triángulo
        
    Raises:
        ValueError: Si la base o la altura son valores negativos o si la base es cero
    """
    if base <= 0:
        if base == 0:
            raise ValueError("La base no puede ser cero")
        else:
            raise ValueError("La base no puede ser un valor negativo")
    
    if altura <= 0:
        raise ValueError("La altura no puede ser un valor negativo")
    
    return (base * altura) / 2 