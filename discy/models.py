from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django_extensions.db.models import TimeStampedModel
from discy.roles import EMPLOYEE_TYPES


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # username = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    # age = models.CharField(max_length=30, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['date_of_birth']
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_full_name(self):
        return "{}{}".format(self.first_name or "", self.last_name or "")


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    question_category = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='question')

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=True, related_name='answer')
    answer_text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return self.answer_text


class Organisation(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'

    def __str__(self):
        return self.name


class UserOrg(TimeStampedModel):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True, blank=True)

    role = models.CharField(max_length=30, null=True, choices=EMPLOYEE_TYPES)

    class Meta:
        verbose_name = 'UserOrg'
        verbose_name_plural = 'UserOrges'

    def __str__(self):
        return self.user.first_name


# class Employee(TimeStampedModel):
#     org_name = models.ManyToManyField('Organisation',through=UserOrg, related_name='Employee')
#     employee = models.ManyToManyField('MyUser', through=UserOrg, related_name='employee')
#     role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
#
#     class Meta:
#         verbose_name = 'Employee'
#         verbose_name_plural = 'Employees'
#
#     def __str__(self):
#         return self.role
