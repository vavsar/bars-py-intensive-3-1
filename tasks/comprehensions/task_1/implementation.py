def flatten_list(matrix: list) -> list:
    """
    Преобразует матрицу (список списков) в линейный список.

    Args:
         matrix: список, элементами которого являются списки

    Returns:
        линейный список
    """
    return [number for nested_list in matrix for number in nested_list]
