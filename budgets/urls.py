from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the softwere_maker view
    path('softwere_maker/', views.softwere_maker, name='softwere_maker'),
    # URL pattern for the expense_anagement_maker view
    path('expense_anagement_maker/', views.expense_anagement_maker, name='expense_anagement_maker'),
    # URL pattern for the group_revenue_maker view
    path('group_revenue_maker/', views.group_revenue_maker, name='group_revenue_maker')
]




