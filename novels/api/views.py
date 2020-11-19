from rest_framework import generics
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from novels.models import Novel,Review
from novels.api.serializers import ReviewSerializer,NovelSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from novels.api.permissions import IsAdminUserOrReadOnly
# from rest_framework.mixins import 
#Novel
class NovelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class NovelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    permission_classes = [IsAdminUserOrReadOnly]

### REVIEW
class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self,serializer):
        novel_pk = self.kwargs.get('novel_pk')
        novel = get_object_or_404(Novel,pk= novel_pk)
        serializer.save(novel = novel)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer












###########################
class NovelList_CreateAPIView(ListModelMixin,CreateModelMixin, generics.GenericAPIView): ##without concrete class
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
