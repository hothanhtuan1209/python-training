from django import forms


class NewDepartmentForm(forms.Form):
    """
    A Django Form class for handling department creation.

    Attributes:
        name (CharField): The name of the department.
        description (CharField): The description of the department.
    """

    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
