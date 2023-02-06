from django.contrib import admin

from methodist.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin[Group]):
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
                    "educational_program"
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
