from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault
from .models import Article


class ArticleSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Article
        fields = ('title', 'content', 'cat', 'user')

