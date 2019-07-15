"""Файл преобразования HTML в текст письма."""

from django.template.loader import render_to_string


def greetings_body(first_name: str, middle_name: str or None) -> str:
    """
    Функция, формирующая HTML-шаблон письма для отправки приветствия.

    :param first_name: имя
    :param middle_name: отчество
    :return: HTML-шаблон, переведенный в строку
    """
    context = {
        'first_name': first_name,
        'middle_name': middle_name,
    }
    return render_to_string('email/greetings.html', context)
