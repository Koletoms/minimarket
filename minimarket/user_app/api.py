from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Profile
from .serializers import ProfileSerializer, AccountSerializer


class ProfileDetailAPIView(APIView):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class AccountDetailAPIView(APIView):
    def get(self, request):
        account = Profile.objects.get(user=request.user)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
