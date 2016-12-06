from django.shortcuts import render


def main(request):
    data = {}
    data['menu_activity_active'] = "active"

    return render(request, 'activity.html', data)

