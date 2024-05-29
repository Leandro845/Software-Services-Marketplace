from celery import shared_task
from .models import SoftwereMaker, ExpenseManagementMaker, GroupRevenueMaker  # Importing models
from django.contrib.messages import constants  # Importing message constants
from django.contrib import messages  # Importing messages module
from .models import Category  # Importing Category model


@shared_task
def softwere_maker_save(name, description, requirements, duration, complexity_id, name_client, phone, email):
    # Retrieving the Category instance based on complexity_id
    complexity = Category.objects.get(id=complexity_id)
    
    # Creating a SoftwereMaker object with the provided data
    softweremaker = SoftwereMaker.objects.create(
        name=name,
        project_description=description,
        project_requirements=requirements,
        project_duration=duration,
        project_complexity=complexity,
        name_surname=name_client,
        phone_number=phone,
        email_client=email,
    )
    
    return softweremaker.id  # Returning the ID of the created SoftwereMaker instance


@shared_task
def expense_anagement_save(company, name_client, email, phone, number_employees, budget_amount, notes):
    # Creating an ExpenseManagementMaker object with the provided data
    expense = ExpenseManagementMaker.objects.create(
        company_name=company,
        contact_name=name_client,
        contact_email=email,
        contact_phone=phone,
        number_of_employees=number_employees,
        budget_amount=budget_amount,
        additional_notes=notes
    )

    return expense.id  # Returning the ID of the created ExpenseManagementMaker instance


@shared_task
def group_revenue_save(name, organization, group_size, revenue_goal, contact_name, email, phone, notes):
    # Creating a GroupRevenueMaker object with the provided data
    group = GroupRevenueMaker.objects.create(
        project_name=name,
        organization_name=organization,
        group_size=group_size,
        revenue_goal=revenue_goal,
        contact_name_second=contact_name,
        contact_email_second=email,
        contact_phone_second=phone,
        additional_notes_second=notes
    )

    return group.id  # Returning the ID of the created GroupRevenueMaker instance
