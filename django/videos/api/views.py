from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from videos.models import Video

# from .permissions import IsOwnerOrReadOnly

from .serializers import (
    VideoListSerializer,
    VideoCreateUpdateSerializer,
    VideoDetailSerializer,
)


class VideoListAPIView(ListAPIView):
    serializer_class = VideoListSerializer
    queryset = Video.objects.all()

class VideoCreateAPIView(CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )

class VideoDetailAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer
    lookup_field = 'unique_id'
