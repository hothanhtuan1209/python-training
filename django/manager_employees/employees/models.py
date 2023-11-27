import uuid

from django.db import models
from enum import Enum

from .constants import GENDER_CHOICES
from departments.models import Department


class ActiveStatus(Enum):
    ACTIVE = "Active"
    DISABLED = "Disabled"


class Employee(models.Model):
    """
    A class representing different employees within the system.

    Attributes:
        id (UUIDField): The primary key for the employee.
        first_name (CharField): The first name of the employee.
        last_name (CharField): The last name of the employee.
        gender (CharField): The gender of the employee.
        birthday (DateField): The employee's birth date.
        email(CharField): The employee's email.
        status (CharField): The status of the employee in company.
        department.id (ForeignKey): This is the department in which
        the employee works
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES, default="Male"
    )
    birthday = models.DateField()
    email = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=10,
        choices=[(status.value, status.value) for status in ActiveStatus],
        default=ActiveStatus.ACTIVE.value,
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE
    )

    def get_full_name(self):
        """
        Combine first name and last name to create the full name of the
        employee.
        """

        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """
        Return a string representation of the Employee object.
        """

        return str(self.get_full_name)
