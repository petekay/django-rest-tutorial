# django-rest-tutorial


Tutorial 4: Authentication & Permissions

Currently our API doesn't have any restrictions on who can edit or delete code snippets. We'd like to have some more advanced behavior in order to make sure that:

    Code snippets are always associated with a creator.
    Only authenticated users may create snippets.
    Only the creator of a snippet may update or delete it.
    Unauthenticated requests should have full read-only access.



http -a admin:password123 POST http://127.0.0.1:8000/snippets/ code="print(789)"


Summary

We've now got a fairly fine-grained set of permissions on our Web API, and end points for users of the system and for the code snippets that they have created.

In part 5 of the tutorial we'll look at how we can tie everything together by creating an HTML endpoint for our highlighted snippets, and improve the cohesion of our API by using hyperlinking for the relationships within the system.