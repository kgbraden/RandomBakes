from django.contrib import admin
from MainPage.models import (highlight,
                             UserProfileInfo,
                             baking_batch,
                             Ingredients,
                             PreFerment,
                             Dough,
                             ShapingFinishing,
                             ActiveSales,
                             Featurette,
                             AboutUs)
# Register your models here.
admin.site.register(highlight)
admin.site.register(UserProfileInfo)
admin.site.register(baking_batch)
admin.site.register(Ingredients)
admin.site.register(PreFerment)
admin.site.register(Dough)
admin.site.register(ShapingFinishing)
admin.site.register(ActiveSales)
admin.site.register(Featurette)
admin.site.register(AboutUs)
