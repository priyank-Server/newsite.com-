from django.conf import settings


def environment_config(request):

    return {
        'user': request.user
    }