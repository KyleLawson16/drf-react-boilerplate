from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

from videos.models import Video

videos_detail_url = HyperlinkedIdentityField(
    view_name='api:detail',
    lookup_field='unique_id'
)

class VideoListSerializer(ModelSerializer):
    url = videos_detail_url
    class Meta:
        model = Video
        fields = [
            'url',
            'id',
            'video_key',
        ]

class VideoCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'video_key',
        ]

class VideoDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Video
        fields = [
            'user',
            'id',
            'video_key',
        ]

    def get_user(self, obj):
        return str(obj.user.username)
