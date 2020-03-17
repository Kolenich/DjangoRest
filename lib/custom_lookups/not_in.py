"""Файл кастомных лукапов в БД."""

from django.db.models.fields import Field
from django.db.models.lookups import In


@Field.register_lookup
class NotIn(In):
    """Кастомный лукап поиска по принципу NOT IN (не содержит)."""

    lookup_name = 'not_in'

    def get_rhs_op(self, connection, rhs):
        """Переопределение метода получения условия выборки при SQL-запросе."""
        return f'NOT IN {rhs}'
