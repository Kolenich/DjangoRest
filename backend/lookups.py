"""Файл кастомных лукапов в БД."""

from django.db.models import Lookup
from django.db.models.fields import Field
from django.db.models.lookups import In


@Field.register_lookup
class NotEqual(Lookup):
    """Кастомный лукап поиска по принципу <> (не равно)."""

    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        """Абстрактный метод трасформации лукапа в SQL запрос."""
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params

        return f'{lhs} <> {rhs}', params


@Field.register_lookup
class NotIn(In):
    """Кастомный лукап поиска по принципу NOT IN (не содержит)."""

    lookup_name = 'not_in'

    def get_rhs_op(self, connection, rhs):
        """Переопределение метода получения условия выборки при SQL-запросе."""
        return f'NOT IN {rhs}'
