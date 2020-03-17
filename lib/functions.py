"""Файл дополнительных функций."""
import os


def split_path(path):
    """
    Функция для разделения пути по папкам.

    :param path: путь, который необходимо разбить
    :return: массив из составных частей
    """
    folders = []
    while True:
        path, folder = os.path.split(path)

        if folder:
            folders.append(folder)
        else:
            if path:
                folders.append(path)

            break

    folders.reverse()

    return folders


def delete_empty_dirs(path: str):
    """
    Функция для рекурсивного удаления всех пустых папок.

    :param path: абсолютный путь до папки, с которой начинать удаление
    """
    # Если переданное значение не является папкой, выходим из функции
    if not os.path.isdir(path):
        return

    children_dirs = [
        os.path.join(path, child_dir) for child_dir in os.listdir(path)
        if os.path.isdir(os.path.join(path, child_dir))
    ]

    if len(children_dirs):
        for child_dir in children_dirs:
            delete_empty_dirs(child_dir)

    # Саму папку media не удаляем
    if not len(os.listdir(path)) and path[-5:] != 'media':
        os.rmdir(path)
