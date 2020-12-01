from django.contrib import admin
from MainPage.models import (highlight,
                             UserProfileInfo,
                             ActiveSales,
                             Featurette,
                             AboutUs, Orders, Customer, Subscription)
# Register your models here.
admin.site.register(highlight)
admin.site.register(UserProfileInfo)
admin.site.register(ActiveSales)
admin.site.register(Featurette)
admin.site.register(AboutUs)
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(Subscription)