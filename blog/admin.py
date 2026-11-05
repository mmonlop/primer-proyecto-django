from django.contrib import admin
from .models import Post
from .models import Autor
from .models import Categoria

# Register your models here.
admin.site.register(Post)
admin.site.register(Autor)
admin.site.register(Categoria)