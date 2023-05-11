def falta_completar_campos(valores):
    """Esta funcion verifica que todos los campos esten completos."""

    return any(map(lambda elem: elem == "" or elem == [], valores.values()))