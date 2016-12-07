from django.shortcuts import render


def main(request):
    data = {}
    data['menu_project_active'] = "active"

    return render(request, 'project.html', data)
