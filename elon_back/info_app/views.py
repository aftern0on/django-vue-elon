from rest_framework.decorators import api_view
from rest_framework.response import Response

from info_app.models import AdvantageBlockCollection, NavigationMenuItem
from info_app.serializers import AdvantageBlockCollectionSerializer, NavigationMenuItemSerializer


@api_view(['GET'])
def get_advantage(request):
    """ Возвращение коллекции блоков с преимуществами
    """

    collection = AdvantageBlockCollection.objects.first()
    serializer = AdvantageBlockCollectionSerializer(collection)
    return Response(serializer.data)


@api_view(['GET'])
def get_navigation_menu(request):
    """Возвращение всех созданных пунктов навигационного меню
    """

    items = NavigationMenuItem.objects.all().order_by('order')
    serializer = NavigationMenuItemSerializer(items, many=True)
    return Response(serializer.data)
