from django.middleware.common import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    
    def __init__(self, get_response=None):
        super().__init__(get_response)
    
    def process_request(self, request):
        # Add logic to execute before the view
        print("Middleware process_request executed")
        # return Response({"error": "Invalid user"}, status=status.HTTP_403_FORBIDDEN)


    def process_response(self, request, response):
        # Add logic to execute after the view
        print("Middleware process_response executed")
        return response
    
    