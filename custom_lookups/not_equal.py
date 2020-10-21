"""Файл кастомных лукапов в БД."""

from django.db.models import Lookup
from django.db.models.fields import Field


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
