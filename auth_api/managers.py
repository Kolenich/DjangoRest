"""Менеджеры для доступа к моделям."""

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Менеджер для модели User, которая используется, как модель по умолчанию."""

    use_in_migrations = True

    def _create_user(self, email: str, password: str, **extra_fields):
        """
        Создание пользователя.

        :param email: почта
        :param password: пароль
        :param extra_fields: дополнительные поля
        :return: созданный пользователь
        """
        if not email:
            raise ValueError('Необходимо указать email.')

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email: str = None, password: str = None, **extra_fields):
        """
        Метод для создания обычного юзера.

        :param email: почта
        :param password: пароль
        :param extra_fields: дополнительные поля
        :return:
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        """
        Метод для создания супер юзера.

        :param email: почта
        :param password: пароль
        :param extra_fields: дополнительные поля
        :return:
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('У супер-пользователя должно быть поле is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('У супер-пользователя должно быть поле is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
