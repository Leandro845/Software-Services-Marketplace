from django.urls import path
from . import views

# URL patterns for budget-related views
urlpatterns = [
    # URL pattern for user login
    path('login/', views.user_login, name='user_login'),
    # URL pattern for displaying software maker budgets
    path('softwere_maker_budgets/', views.softwere_maker_budgets, name='softwere_maker_budgets'),
    # URL pattern for displaying expense management maker budgets
    path('expense_management_maker_budget/', views.expense_management_maker_budget, name='expense_management_budget'),
    # URL pattern for displaying group revenue maker budgets
    path('group_revenue_maker_budget/', views.group_revenue_maker_budget, name='group_revenue_maker_budget')
]
