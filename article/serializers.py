from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.author
    class Meta:
        model = Article
        fields = '__all__'