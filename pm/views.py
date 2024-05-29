from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.messages import constants, messages
from django.core.paginator import Paginator
from budgets.models import SoftwereMaker, ExpenseManagementMaker, GroupRevenueMaker
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# View for user login
def user_login(request):
    # Handling GET request to display login page
    if request.method == 'GET':
        return render(request, 'login.html')
    
    # Handling POST request for user authentication
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user credentials
        user = authenticate(request, username=username, password=password)

        # If user authentication fails, display error message
        if not user:
            messages.add_message(request, constants.ERROR, '❌ Invalid username or password ')
            return redirect('user_login')
        
        # If user authentication succeeds, log in the user
        login(request, user)

        return redirect('softwere_maker_budgets')

# View for budget manager dashboard
@login_required(login_url='user_login')
def budget_manager(request):
    # Render the budget manager dashboard
    return render(request, 'budget_manager.html')

# View for displaying software maker budgets
@login_required(login_url='user_login')
def softwere_maker_budgets(request):
    search_term = request.GET.get('search', '')

    # Filtering software maker budgets based on search term
    if search_term:
        softwere_makers = SoftwereMaker.objects.filter(
            Q(name__icontains=search_term) |
            Q(project_description__icontains=search_term) |
            Q(project_requirements__icontains=search_term) |
            Q(project_complexity__name_category__icontains=search_term) |
            Q(name_surname__icontains=search_term) |
            Q(phone_number__icontains=search_term) |
            Q(email_client__icontains=search_term) 
        )
    else:
        softwere_makers = SoftwereMaker.objects.all()

    paginator = Paginator(softwere_makers, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    variables = {
        'page_obj': page_obj,
        'search_term': search_term
    }
    return render(request, 'softwere_maker_budgets.html', variables)

# View for displaying expense management maker budgets
@login_required(login_url='user_login')
def expense_management_maker_budget(request):
    search_term = request.GET.get('search', '')

    # Filtering expense management maker budgets based on search term
    if search_term:
        expense_management = ExpenseManagementMaker.objects.filter(
            Q(company_name__icontains=search_term) |
            Q(contact_name__icontains=search_term) |
            Q(contact_email__icontains=search_term) |
            Q(contact_phone__icontains=search_term) |
            Q(number_of_employees__icontains=search_term) |
            Q(budget_amount__icontains=search_term) |
            Q(additional_notes__icontains=search_term) 
        )
    else:
        expense_management = ExpenseManagementMaker.objects.all()

    paginator = Paginator(expense_management, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    variables = {
        'page_obj': page_obj,
    }
    return render(request, 'expense_management_maker_budget.html', variables)

# View for displaying group revenue maker budgets
@login_required(login_url='user_login')
def group_revenue_maker_budget(request):
    search_term = request.GET.get('search', '')

    # Filtering group revenue maker budgets based on search term
    if search_term:
        group_revenue_maker = GroupRevenueMaker.objects.filter(
            Q(project_name__icontains=search_term) |
            Q(organization_name__icontains=search_term) |
            Q(group_size__icontains=search_term) |
            Q(revenue_goal__icontains=search_term) |
            Q(contact_name_second__icontains=search_term) |
            Q(contact_email_second__icontains=search_term) |
            Q(contact_phone_second__icontains=search_term) |
            Q(additional_notes_second__icontains=search_term)
        )
    else:
        group_revenue_maker = GroupRevenueMaker.objects.all()

    paginator = Paginator(group_revenue_maker, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    variables = {
        'page_obj': page_obj,
    }
    return render(request, 'group_revenue_maker_budget.html', variables)
