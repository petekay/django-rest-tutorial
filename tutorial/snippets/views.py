from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

"""
Using generic class-based views

Using the mixin classes we've rewritten the views to use slightly less code than before, but we can go one step further. 
REST framework provides a set of already mixed-in generic views that we can use to trim down our views.py module even more.

"""

"""
Associating Snippets with Users

Right now, if we created a code snippet, there'd be no way of associating the user that created the snippet, with the snippet instance. 
The user isn't sent as part of the serialized representation, but is instead a property of the incoming request.

The way we deal with that is by overriding a .perform_create() method on our snippet views, that allows us to modify how the instance save is managed, 
and handle any information that is implicit in the incoming request or requested URL.

On the SnippetList view class, add the following method:
"""

"""
We'll also add a couple of views to views.py. 
We'd like to just use read-only views for the user representations, so we'll use the ListAPIView and RetrieveAPIView generic class-based views.
"""

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    