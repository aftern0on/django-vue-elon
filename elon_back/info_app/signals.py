from django.db.models.signals import post_migrate
from django.dispatch import receiver

from info_app.models import AdvantageBlock, AdvantageBlockCollection, NavigationMenuItem


@receiver(post_migrate)
def create_default_objects(sender, **kwargs):
    # Создание блоков преимуществ по умолчанию
    if not AdvantageBlock.objects.exists():
        block_1 = AdvantageBlock.objects.create()
        block_2 = AdvantageBlock.objects.create()
        block_3 = AdvantageBlock.objects.create()
        block_4 = AdvantageBlock.objects.create()

        # Создание коллекции блоков преимуществ по умолчанию
        if not AdvantageBlockCollection.objects.exists():
            AdvantageBlockCollection.objects.create(
                block_one=block_1,
                block_two=block_2,
                block_three=block_3,
                block_four=block_4)

    # Создание ссылок навигационного меню
    if not NavigationMenuItem.objects.exists():
        NavigationMenuItem.objects.create(order=0, name='Главная')
        NavigationMenuItem.objects.create(order=1, name='Технология', href='/tech')
        NavigationMenuItem.objects.create(order=2, name='График полетов', href='/graphic')
        NavigationMenuItem.objects.create(order=3, name='Гарантии', href='/grants')
        NavigationMenuItem.objects.create(order=4, name='О нас', href='/about')
        NavigationMenuItem.objects.create(order=5, name='Контакты', href='/contacts')
