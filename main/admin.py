from django.contrib import admin

from main.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'language', 'grades', 'gender')
    list_filter = ('language', 'gender', 'grades')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


admin.site.register(Student, StudentAdmin)
