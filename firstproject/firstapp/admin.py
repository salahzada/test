from django.contrib import admin
from firstapp.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    model=UserProfile
    # fieldsets = (
    #     ('Personal info', {'fields': (
    #         'name',)}),
    # )

    # def product_count(self, obj):
    #     return obj.product_set.count()
    # product_count.short_description = 'Product Count'

    list_display = ('id','name','surname','address','fincode','register_type','phone','email','desc','attachment')
    search_fields = ('name','surname','address','fincode','phone','email','attachment')
    ordering = ('id',)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "register_type":
            kwargs['choices'] = (
                ('İnvestor', 'İnvestor'),
                ('Emitent', 'Emitent'),
                ('İnvestisiya şirkəti', 'İnvestisiya şirkəti'),
            )
        return super().formfield_for_choice_field(db_field, request, **kwargs)

admin.site.register(UserProfile,UserProfileAdmin)