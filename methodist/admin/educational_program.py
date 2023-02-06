from django.contrib import admin

from methodist.models import EducationalProgram


@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin[EducationalProgram]):
    list_display = ("id", "name", "__str__")
    list_display_links = ("id", "name", "__str__")

    search_fields = ("name",)
    readonly_fields = ["created", "modified"]

    fieldsets = [
        (
            'Main data',
            {
                'fields': [
                    'name',
                    "department"
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
