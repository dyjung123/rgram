from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all() # 모든 이미지의 오브젝트를 다 들구와라
    
        serializer = serializers.ImageSerializer(all_images, many=True)
        
        return Response(data=serializer.data)

class ListAllComment(APIView):

    def get(self, request, format=None):

        all_comments = models.Comment.objects.all() # 모든 이미지의 오브젝트를 다 들구와라
    
        serializer = serializers.CommentSerializer(all_comments, many=True)
        
        return Response(data=serializer.data)

class ListAllLike(APIView):

    def get(self, request, format=None):

        all_likes = models.Like.objects.all() # 모든 이미지의 오브젝트를 다 들구와라
    
        serializer = serializers.LikeSerializer(all_likes, many=True)
        
        return Response(data=serializer.data)