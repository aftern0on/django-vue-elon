from django.contrib import admin
from .models import AdvantageBlock, AdvantageBlockCollection, NavigationMenuItem


class AdvantageBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'first', 'middle', 'last')


class AdvantageBlockCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'block_one', 'block_two', 'block_three', 'block_four')
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False


class NavigationMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'href', 'order')
    ordering = ('order',)


admin.site.register(AdvantageBlock, AdvantageBlockAdmin)
admin.site.register(AdvantageBlockCollection, AdvantageBlockCollectionAdmin)
admin.site.register(NavigationMenuItem, NavigationMenuAdmin)
