from django.shortcuts import render


def main(request):
    data = {}
    data['menu_profile_active'] = "active"

    return render(request, 'profile.html', data)
