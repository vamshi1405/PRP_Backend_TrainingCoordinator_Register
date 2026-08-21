from django.contrib import admin
from .models import TrainingCoordinator

@admin.register(TrainingCoordinator)
class TrainingCoordinatorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "official_email",
        "phone_number",
        "employee_id",
        "designation",
    )

    search_fields = (
        "full_name",
        "official_email",
        "employee_id",
    )

    list_filter = ("designation",)