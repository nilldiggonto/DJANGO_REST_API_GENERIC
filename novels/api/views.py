from rest_framework import generics
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from novels.models import Novel,Review
from novels.api.serializers import ReviewSerializer,NovelSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from novels.api.permissions import IsAdminUserOrReadOnly,IsReviewAuthorOrReadOnly
from rest_framework.exceptions import ValidationError
from novels.api.paginations import PageNumberPagination,SmallPagination
# from rest_framework.mixins import 
#Novel
class NovelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Novel.objects.all().order_by('-id')
    serializer_class = NovelSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallPagination


class NovelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    permission_classes = [IsAdminUserOrReadOnly]

### REVIEW
class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        novel_pk = self.kwargs.get('novel_pk')
        novel = get_object_or_404(Novel,pk= novel_pk)
        review_author = self.request.user

        review_qs = Review.objects.filter(novel=novel,review_author=review_author)
        if review_qs.exists():
            raise ValidationError('Already Reviewd this novel')


        serializer.save(novel = novel,review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]












###########################
class NovelList_CreateAPIView(ListModelMixin,CreateModelMixin, generics.GenericAPIView): ##without concrete class
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
