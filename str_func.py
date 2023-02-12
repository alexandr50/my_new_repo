def get_upper(text: str):
    """Функция преобразующая весь текст в заглавные буквы
    что там еще"""
    result = text.upper()
    return result


def get_tilte(text: str):
    """ Функция преобразующая первые буквы каждого слова в заглавные"""

    return ' '.join([x.title() for x in text.split(' ')])


