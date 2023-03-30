from django.http import JsonResponse
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from django.views.decorators.csrf import csrf_exempt

from generic_commands.services import roll
from errors import errors


@authentication_classes([])
@permission_classes([])
@csrf_exempt
def post(request):
    lower_bound = int(request.POST.get('lower_bound', None))
    upper_bound = int(request.POST.get('upper_bound', None))
    request_obj = {'lower_bound': lower_bound, 'upper_bound': upper_bound}
    result = roll.Roll(request_obj).__dict__
    breakpoint()
    return JsonResponse(result)


