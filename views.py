from django.shortcuts import render
from .models import Standup


# Create your views here.
def index(request):

    if request.method == 'POST':
        yesterday = request.POST.get('yesterday', '')
        today = request.POST.get('today', '')
        blocker = request.POST.get('blocker', '')
        user = None

        if request.user.is_authenticated():
            user = request.user

        standup = Standup.objects.create(
            yesterday=yesterday,
            today=today,
            blocker=blocker,
            user=user
        )
        return render(request, 'standups/index.html')

    context = {}
    if request.user.is_authenticated():
        user = request.user
        context['user_standups'] = user.standups.all()
        user_company = user.companies.last()

        if user in user_company.admins.all():

            is_admin = True

            company_standups = user_company.get_standups()
            context['company_standups'] = company_standups
            context['is_admin'] = is_admin


    return render(request, 'standups/index.html', context)
