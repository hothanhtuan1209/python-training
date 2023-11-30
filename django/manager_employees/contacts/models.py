import uuid

from django.db import models
from django.core.validators import RegexValidator

from employees.models import Employee


class Contact(models.Model):
    """
    A class representing different roles within the system.

    Attributes:
        id (UUIDField): The primary key for the employee.
        phone_number (CharField): The employee's phone number.
        address (CharField): The employee's address
        employee (ForeignKey): the instance of employee whom the
        contact belongs.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4
    )
    phone_number = models.CharField(
        validators=[RegexValidator(r"^0\d{9}$")], max_length=10
    )
    address = models.CharField(max_length=100)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE
    )
