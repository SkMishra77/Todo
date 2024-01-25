import hashlib
import random
import string
import time

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


def response_fun(*args):
    if args[0] == 1:
        # args[1]['status_code'] = STATUS_OK
        return Response({'error': False, 'responseData': args[1], 'status_code': status.HTTP_200_OK})
    else:
        return Response(
            {'error': True, 'message': args[1], 'status_code': status.HTTP_400_BAD_REQUEST})


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class Util:
    @staticmethod
    def generateTaskId():
        # Generate a unique identifier based on epoch time
        epoch_time = str(int(time.time()))

        # Generate 12 random characters
        random_chars = ''.join(
            random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))

        # Combine all the components
        unique_string = f"{epoch_time}_{random_chars}"

        # Hash the unique string using SHA-256
        hash_object = hashlib.md5(unique_string.encode())
        hash_string = "Task_" + hash_object.hexdigest()

        return hash_string
