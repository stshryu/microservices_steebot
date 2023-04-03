from rest_framework.test import APIRequestFactory


def api_factory_helper(request_type: str, request_data: dict = None):
    factory = APIRequestFactory()
    if request_type == 'post':
        request = factory.post('', request_data)
    elif request_type == 'get':
        request = factory.get('')
    return request