from rest_framework.serializers import ModelSerializer

from info_app.models import AdvantageBlock, AdvantageBlockCollection, NavigationMenuItem


class AdvantageBlockSerializer(ModelSerializer):
    class Meta:
        model = AdvantageBlock
        fields = ("first", "middle", "last")


class AdvantageBlockCollectionSerializer(ModelSerializer):
    block_one = AdvantageBlockSerializer()
    block_two = AdvantageBlockSerializer()
    block_three = AdvantageBlockSerializer()
    block_four = AdvantageBlockSerializer()

    class Meta:
        model = AdvantageBlockCollection
        fields = ('block_one', 'block_two', 'block_three', 'block_four')


class NavigationMenuItemSerializer(ModelSerializer):
    class Meta:
        model = NavigationMenuItem
        fields = ('order', 'name', 'href')
