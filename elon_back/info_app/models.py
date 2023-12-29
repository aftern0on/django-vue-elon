from django.db import models


class NavigationMenuItem(models.Model):
    """Пункт в навигационном меню

    Attributes:
        name (CharField): Наименование пункта
        href (CharField): Ссылка, на которую указывает пункт
    """

    name = models.CharField(max_length=255, default='Ссылка')
    href = models.CharField(max_length=255, default='/')
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}: {self.href}"


class AdvantageBlock(models.Model):
    """Информационный блок для преимущества

    Attributes:
        first (CharField): первая строчка
        middle (CharField): строчка по середине
        last (CharField): последняя строчка
    """

    first = models.CharField(max_length=255, default="Первая строчка")
    middle = models.CharField(max_length=255, default="100%")
    last = models.CharField(max_length=255, default="Последняя строчка")

    def __str__(self):
        return f"{self.first} {self.middle} {self.last}"


class AdvantageBlockCollection(models.Model):
    """Коллекция блоков преимуществ

    Attributes:
        block_one (AdvantageBlock): первый блок
        block_two (AdvantageBlock): второй блок
        block_three (AdvantageBlock): третий блок
        block_four (AdvantageBlock): четвертый блок
    """

    block_one = models.ForeignKey(AdvantageBlock, related_name="block_one_set", on_delete=models.CASCADE)
    block_two = models.ForeignKey(AdvantageBlock, related_name="block_two_set", on_delete=models.CASCADE)
    block_three = models.ForeignKey(AdvantageBlock, related_name="block_three_set", on_delete=models.CASCADE)
    block_four = models.ForeignKey(AdvantageBlock, related_name="block_four_set", on_delete=models.CASCADE)