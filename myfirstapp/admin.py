from django.contrib import admin

# Register your models here.


from myfirstapp.models import complaint
admin.site.register(complaint)


from myfirstapp.models import complaint_register 
admin.site.register(complaint_register)



from myfirstapp.models import super_user_details
admin.site.register(super_user_details)



