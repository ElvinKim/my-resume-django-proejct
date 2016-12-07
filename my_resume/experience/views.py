from django.shortcuts import render


def main(request):
    data = {}
    data['menu_experience_active'] = "active"

    return render(request, 'experience.html', data)
