from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email має бути встановлений")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser має бути is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser має бути is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30, verbose_name="Ім'я")
    surname = models.CharField(max_length=30, verbose_name="Прізвище")
    phone = models.CharField(max_length=14, verbose_name="Телефон")
    address = models.CharField(max_length=100, verbose_name="Адреса")
    email = models.EmailField(max_length=100, verbose_name="Електронна пошта", unique=True)
    # password = models.CharField(max_length=100, blank=True, verbose_name="Пароль")

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name','surname','address','phone']

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    def __str__(self):
        return f"{self.phone} ({self.name})"

