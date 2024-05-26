
from rest_framework import serializers

from main.models import Post

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [ "id","title", "slug", "category", "description", "short_description"]
    
    
    


