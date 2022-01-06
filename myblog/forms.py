from django.forms import modelform_factory, DecimalField

from .models import Post

form_model = modelform_factory(Post, fields=('title', 'text', 'age', 'date_born'))