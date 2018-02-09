from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Article)
admin.site.register(ContactInfo)
admin.site.register(Introduce_content)
admin.site.register(Fee_content)
admin.site.register(Join_form)
admin.site.register(Key_word)

admin.site.register(Introduce_Keyword)
admin.site.register(Fee_Keyword)
admin.site.register(MainPage_article)
admin.site.register(JoinPage_detail)
admin.site.register(Friend_link)