from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from django.views.decorators.csrf import csrf_exempt

from generic_commands.services import roll, flip
from errors import errors
import success


@api_view(['POST'])
def diceroll(request):
    roll_obj = roll.Roll()
    result = roll_obj.perform_roll(request)

    match result:
        case errors.InvalidInputs():
            content = {'Error': result.__dict__}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        case errors.MissingInputs():
            content = {'Error': result.__dict__}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        case success.Success():
            content = {'Success': result.unpack().__dict__}
            return Response(content, status=status.HTTP_200_OK)
        case _:
            content = {'Error': errors.UnexpectedError.__dict__}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def coinflip(request):
    flip_obj = flip.Flip()
    result = flip_obj.perform_flip()

    match result:
        case success.Success():
            content = {'Success': result.unpack().__dict__}
            return Response(content, status=status.HTTP_200_OK)
        case _:
            content = {'Error': errors.UnexpectedError.__dict__}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
