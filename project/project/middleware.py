from django.utils.decorators import async_middleware


@async_middleware
def async_test_middleware(get_response):

    async def middleware(request):
        response = await get_response(request)
        response.i_did_something = True
        return response

    return middleware
