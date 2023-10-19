from debugapp.models import FlockClient

class FlockEventListener:

    def __init__(self, request):

        self.request = request


    def app_install(self):


        client, created = FlockClient.objects.get_or_create(user_id=self.request.data['userId'])
        client.token = self.request.data['token']
        client.user_token = ''
        client.save()

