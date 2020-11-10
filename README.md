## django-rest-tutorial

# Tutorial 6: ViewSets & Routers

Registering the viewsets with the router is similar to providing a urlpattern. We include two arguments - the URL prefix for the views, and the viewset itself.

The DefaultRouter class we're using also automatically creates the API root view for us, so we can now delete the api_root method from our views module.
Trade-offs between views vs viewsets

Using viewsets can be a really useful abstraction. It helps ensure that URL conventions will be consistent across your API, minimizes the amount of code you need to write, and allows you to concentrate on the interactions and representations your API provides rather than the specifics of the URL conf.

That doesn't mean it's always the right approach to take. There's a similar set of trade-offs to consider as when using class-based views instead of function based views. Using viewsets is less explicit than building your views individually.