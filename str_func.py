def get_upper(text: str):
    """Функция преобразующая текст в заглавные буквы и еще что-то"""
    return text.upper()


def get_tilte(text: str):
    """ Функция преобразующая первые буквы каждого слова в заглавные"""

    result = ' '.join([x.title() for x in text.split(' ')])
    return result


