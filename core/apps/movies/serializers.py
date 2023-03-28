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

    def get_user(self, movie):
        user = movie.user
        return {
            'user_type': user.user_type,
            'email': user.email
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = self.get_user(instance)
        return rep

    class Meta:
        model = Movie
        fields = [
            "title", "tags", "user", "description", "release_date"
        ]