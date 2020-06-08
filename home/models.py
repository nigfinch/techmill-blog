from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# redirect from homepage to blog. We can add a website hompege later if required 
from django.http import HttpResponseRedirect



class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def serve(self, request):
        # Redirect to blog index page
        return HttpResponseRedirect('/blog/')

        # only do this if you're using urls.py and namespaces
        # return HttpResponseRedirect(reverse('blog:index'))