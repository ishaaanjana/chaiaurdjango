from django.contrib import admin
from .models import ChaiVarity, ChaiReview, Store, ChaiCertificate

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    # filter_horizontal = ('chai_varities',)  

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai',)  

# Register models
admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)