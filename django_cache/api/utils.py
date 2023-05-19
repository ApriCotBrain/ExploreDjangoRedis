import redis

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

# Создаем экземпляр Redis
redis_instance = redis.StrictRedis.from_url(
    settings.CACHES['default']['LOCATION'])


def set_jwt_token_to_redis(token, user_id):
    """
    Кэширует токен в Redis.
    Метод `set()` используется для сохранения значения `user_id`
    в Redis по ключу `token`.
    Формат команды: `redis_instance.set(key, value, ex=expire_time)`.
    Где `key` - ключ, по которому сохраняется значение,
    `value` - сохраняемое значение,
    а `ex` - время жизни ключа в секундах.
    """
    redis_instance.set(token, user_id, ex=60 * 60 * 24)


def get_user_id_from_jwt_token_from_redis(token):
    """
    Получает идентификатор пользователя (`user_id`) из JWT-токена,
    сохраненного в Redis.
    """
    user_id = redis_instance.get(token)
    # Если `user_id` найден в Redis,
    # то декодируем его из `bytes` в строковое значение.
    # (так как в Redis все значения хранятся в бинарном виде)
    if user_id:
        return user_id.decode('utf-8')
    else:
        # Если user_id не найден в Redis, пробуем получить его из БД
        try:
            user = User.objects.get(auth_token=token)
            # Сохраняем user_id в Redis
            set_jwt_token_to_redis(token, user.id)
            return user.id
        except User.DoesNotExist:
            # Если user_id не найден в Redis и БД,
            # то возможно токен истек или неправильный
            return None
