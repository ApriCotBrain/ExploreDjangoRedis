import time

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from api.utils import (
    set_jwt_token_to_redis,
    get_user_id_from_jwt_token_from_redis
)


# Декоратор `@csrf_exempt` отключает защиту от CSRF-атак,
# то есть для выполнения запроса к данной функции не нужно
# предоставлять CSRF-токен.
@csrf_exempt
def set_jwt_token(request):
    """
    Сохраняет пары значений токена и
    идентификатора пользователя в Redis.
    """
    if request.method == 'POST':
        # Получаем значение токена и user_id
        data = json.loads(request.body)
        token = data.get('token')
        user_id = data.get('user_id')

        # Замеряем время выполнения функции с помощью time.time()
        start_time = time.time()

        # Сохраняем в Redis
        set_jwt_token_to_redis(token, user_id)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")

        return HttpResponse('Token has been saved to Redis cache.')
    else:
        return HttpResponse('Invalid request method.')


@csrf_exempt
def get_user_id_from_jwt_token(request):
    """
    Получает идентификатор пользователя (`user_id`) из JWT-токена.
    """
    if request.method == 'POST':
        # Получаем значение токена
        data = json.loads(request.body)
        token = data.get('token')

        # Замеряем время выполнения функции с помощью time.time()
        start_time = time.time()

        # Ищем в Redis идентификатор пользователя (`user_id`)
        # по JWT-токену (`token`).
        user_id = get_user_id_from_jwt_token_from_redis(token)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")

        if user_id:
            return HttpResponse(user_id)
        else:
            return HttpResponse('Invalid JWT token.')
    else:
        return HttpResponse('Invalid request method.')
