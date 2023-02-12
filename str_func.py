def get_upper(text: str):
    """Функция преобразующая текст в заглавные буквы"""
    return text.upper()


def get_tilte(text: str):
    """ Функция преобразующая первые буквы каждого слова в заглавные"""

    return ' '.join([x.title() for x in text.split(' ')])


