from django.db import models


class Category:
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self', null=True, related_name="children", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    images = models.ManyToManyField("ProductImage")


class ProductVariant(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    name = models.TextField(max_length=255, blank=True)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    source = models.TextField(max_length=255, blank=False)


