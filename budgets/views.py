from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from .tasks import softwere_maker_save, expense_anagement_save, group_revenue_save
from .models import Category


def softwere_maker(request): 
    # Render the form with categories for project complexity
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'softwere_maker.html', {'categories': categories})
    
    # Process form submission
    elif request.method == 'POST':
        # Extract form data
        name = request.POST.get('project-name')
        project_description = request.POST.get('project-description')
        project_requirements = request.POST.get('project-requirements')
        project_duration = request.POST.get('project-duration')
        project_complexity = request.POST.get('project-complexity')
        name_surname = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email_client = request.POST.get('email')

        # Check if all required fields are filled
        if not all([name, project_description, project_requirements,
                    project_duration, project_complexity, name_surname,
                    phone_number, email_client]):
            messages.add_message(request, constants.ERROR, '❌ All fields must be filled out.')
            return redirect('softwere_maker')

        try:
            # Get the category object for project complexity
            project_complexity_category = Category.objects.get(name_category__iexact=project_complexity) 
        except Category.DoesNotExist:
            # If category does not exist, show error message
            messages.add_message(request, constants.ERROR, f'❌ The category "{project_complexity}" does not exist.')
            return redirect('softwere_maker')

        # Save form data asynchronously
        softwere_maker_save.delay(
            name,
            project_description,
            project_requirements,
            project_duration,
            project_complexity_category.id,
            name_surname,
            phone_number,
            email_client,
        )        

        # Show success message
        messages.add_message(request, constants.SUCCESS, 'Your budget form has been successfully submitted! 🎉')

        return render(request, 'softwere_maker.html')


def expense_anagement_maker(request): 
    if request.method == 'GET':
        return render(request, 'expense_management_maker.html')
    
    elif request.method == 'POST':
        # Extract form data
        company_name = request.POST.get('company-name')
        contact_name = request.POST.get('contact-name')
        contact_email = request.POST.get('contact-email')
        contact_phone = request.POST.get('contact-phone')
        number_of_employees = request.POST.get('employees-number')
        budget_amount = request.POST.get('budget-amount')
        additional_notes = request.POST.get('additional-notes')

        # Check if all required fields are filled
        if not all([company_name, contact_name, contact_email,
                   contact_phone, number_of_employees, budget_amount,
                   additional_notes]):
            messages.add_message(request, constants.ERROR, '❌ All fields must be filled out.')
            return redirect('expense_anagement_maker')

        # Save form data asynchronously
        expense_anagement_save.delay(
            company_name,
            contact_name,
            contact_email,
            contact_phone,
            number_of_employees,
            budget_amount,
            additional_notes
        )

        # Show success message
        messages.add_message(request, constants.SUCCESS, 'Your budget form has been successfully submitted! 🎉')

        return render(request, 'expense_management_maker.html')


def group_revenue_maker(request): 
    if request.method == 'GET':
        return render(request, 'group_revenue_maker.html')

    elif request.method == 'POST':
        # Extract form data
        project_name = request.POST.get('project-name')
        organization_name = request.POST.get('organization-name')
        group_size = request.POST.get('group-size')
        revenue_goal = request.POST.get('revenue-goal')
        contact_name_second = request.POST.get('contact_name')
        contact_email_second = request.POST.get('contact_email')
        contact_phone_second = request.POST.get('contact_phone')
        additional_notes_second = request.POST.get('additional_notes')

        # Check if all required fields are filled
        if not all([project_name, organization_name, group_size,
                    revenue_goal, contact_name_second, contact_email_second,
                    contact_phone_second, additional_notes_second]):
            messages.add_message(request, constants.ERROR, '❌ All fields must be filled out.')
            return redirect('group_revenue_maker')

        # Save form data asynchronously
        group_revenue_save.delay(
            project_name,
            organization_name,
            group_size,
            revenue_goal,
            contact_name_second,
            contact_email_second,
            contact_phone_second,
            additional_notes_second
        )

        # Show success message
        messages.add_message(request, constants.SUCCESS, 'Your budget form has been successfully submitted! 🎉')

        return render(request, 'group_revenue_maker.html')
