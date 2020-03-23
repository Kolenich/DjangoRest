"""Файл преобразования HTML в текст письма."""

from django.template.loader import render_to_string


def greetings_body(task: dict, assigned_by: str) -> str:
    """
    Функция, формирующая HTML-шаблон письма для отправки приветствия.

    :param task: объект задачи
    :param assigned_by: иям и фамилия назначившего
    :return: HTML-шаблон, переведенный в строку
    """
    context = {'assigned_by': assigned_by, **task}
    return render_to_string('email/greetings.html', context)
