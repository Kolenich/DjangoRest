"""Файл классов-примесей."""

from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.response import Response


class CustomModelViewSet(viewsets.ModelViewSet):
    """Класс-примесь для ModelViewset."""

    def get_paginated_list(self, queryset: QuerySet) -> Response:
        """
        Общий метод отдачи данных на основании переданного кверисета.

        :param queryset: кверисет
        :return: объект ответа с обработанными данными
        """
        filtered_queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(filtered_queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)
