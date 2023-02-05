from django.contrib import admin

from methodist.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin[Department]):
    list_display = ("id", "name", "__str__")
    list_display_links = ("id", "name", "__str__")

    search_fields = ("name",)
    readonly_fields = ["created", "modified"]

    fieldsets = [
        (
            'Name Department',
            {
                'fields': [
                    'name'
                ],
            },
        ),
        (
            'Datetime',
            {
                'fields': [
                    'created',
                    'modified'
                ],
            },
        ),
    ]
