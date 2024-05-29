# Import necessary modules
from django.contrib import admin
from .models import Category, SoftwereMaker, ExpenseManagementMaker, GroupRevenueMaker

# Define admin classes for each model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')

class SoftwereMakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 12

class ExpenseManagementAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')
    list_display_links = ('id', 'company_name')
    list_per_page = 12

class GroupRevenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name')
    list_display_links = ('id', 'project_name')
    list_per_page = 12

# Register admin classes for each model
admin.site.register(SoftwereMaker, SoftwereMakerAdmin)
admin.site.register(ExpenseManagementMaker, ExpenseManagementAdmin)
admin.site.register(GroupRevenueMaker, GroupRevenueAdmin)
admin.site.register(Category, CategoryAdmin)
