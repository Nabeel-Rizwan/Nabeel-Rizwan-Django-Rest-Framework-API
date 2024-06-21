from django.contrib import admin
from app.models import User

class User_Admin(admin.ModelAdmin):
    list_display=('name','Identification_ID','number','personal_number','spam')     ## List Feature Overview on Admin Panel
    search_fields = ['name', 'number','personal_number']        ## Features to be searched


admin.site.register(User,User_Admin)        ## Register in Admin Panel
