from .models import Post
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'slug', 'image', 'content','publish','updated')