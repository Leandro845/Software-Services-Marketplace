from django.db import models


class Category(models.Model):
    # Define a category model to represent project complexity categories.
    name_category = models.CharField(max_length=100)  # Field to store the name of the category.

    def __str__(self) -> str:
        # Return the name of the category when the object is converted to a string.
        return self.name_category


class SoftwereMaker(models.Model):
    # Define a model for software project details and client information.
    name = models.CharField(max_length=100)  # Field to store the name of the project.
    project_description = models.TextField(max_length=1200)  # Field to store project description.
    project_requirements = models.TextField(max_length=1200)  # Field to store project requirements.
    project_duration = models.IntegerField()  # Field to store project duration.
    project_complexity = models.ForeignKey(Category, on_delete=models.CASCADE)  # Relationship with Category model.

    # Personal data
    name_surname = models.CharField(max_length=100)  # Field to store client's name and surname.
    phone_number = models.CharField(max_length=20)  # Field to store client's phone number.
    email_client = models.EmailField(max_length=70)  # Field to store client's email.

    def __str__(self) -> str:
        # Return the name of the project when the object is converted to a string.
        return self.name
    

class ExpenseManagementMaker(models.Model):
    # Define a model for expense management project details and client information.
    company_name = models.CharField(max_length=100)  # Field to store the name of the company.
    contact_name = models.CharField(max_length=70)  # Field to store contact person's name.
    contact_email = models.EmailField(max_length=70)  # Field to store contact person's email.
    contact_phone = models.CharField(max_length=20)  # Field to store contact person's phone number.
    number_of_employees = models.IntegerField()  # Field to store number of employees.
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Field to store budget amount.
    additional_notes = models.TextField(max_length=1200)  # Field to store additional notes.

    def __str__(self) -> str:
        # Return the name of the company when the object is converted to a string.
        return self.company_name
    

class GroupRevenueMaker(models.Model):
    # Define a model for group revenue project details and client information.
    project_name = models.CharField(max_length=100)  # Field to store the name of the project.
    organization_name = models.CharField(max_length=70)  # Field to store organization's name.
    group_size = models.IntegerField()  # Field to store group size.
    revenue_goal = models.DecimalField(max_digits=10, decimal_places=2)  # Field to store revenue goal.
    contact_name_second = models.CharField(max_length=70)  # Field to store contact person's name.
    contact_email_second = models.EmailField(max_length=70)  # Field to store contact person's email.
    contact_phone_second = models.CharField(max_length=20)  # Field to store contact person's phone number.
    additional_notes_second = models.TextField(max_length=1200)  # Field to store additional notes.

    def __str__(self) -> str:
        # Return the name of the project when the object is converted to a string.
        return self.project_name
