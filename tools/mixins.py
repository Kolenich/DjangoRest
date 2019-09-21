"""Файл классов-примесей."""

from rest_framework import viewsets
from rest_framework.response import Response


class CustomListMixin(viewsets.ModelViewSet):
    """Класс-примесь для ModelViewset."""

    def custom_list(self, queryset) -> Response:
        """
        Кастомный метод отдачи данных на основании переданного кверисета.

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
