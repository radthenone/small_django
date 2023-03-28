from rest_framework import serializers
from apps.movies.models import Movie, Tag
from apps.users.models import User
from apps.users.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    user = serializers.SerializerMethodField()

    def get_user(self, user):
        users = User.objects.filter(pk=user.pk)
        serializer = UserSerializer(users, many=True)
        return serializer.data
    class Meta:
        model = Movie
        fields = [
            "title", "tags", "user", "description", "release_date"
        ]