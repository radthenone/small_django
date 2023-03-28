from rest_framework import viewsets
from rest_framework import generics
from apps.movies.models import Movie, Tag
from apps.movies.serializers import MovieSerializer, TagSerializer
from apps.users.permissions import PublicPermission, OwnerPermission, SuperuserPermission

# Create your views here.

class MovieList(generics.ListAPIView):
    permission_classes = [PublicPermission]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveAPIView):
    permission_classes = [SuperuserPermission]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateView(generics.CreateAPIView):
    permission_classes = [SuperuserPermission]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdateView(generics.UpdateAPIView):
    permission_classes = [OwnerPermission]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [PublicPermission]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
class TagCreateViewSet(generics.CreateAPIView):
    permission_classes = [PublicPermission]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TaggedMovieList(generics.ListAPIView):
    permission_classes = [PublicPermission]
    serializer_class = MovieSerializer

    def get_queryset(self):
        tag = self.kwargs['tag']
        return Movie.objects.filter(tags__name__icontains=tag)