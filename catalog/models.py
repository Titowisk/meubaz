from django.db import models
from django.urls import reverse


class Category(models.Model):

    # nome da categoria
    name = models.CharField('Nome', max_length=100)
    # slug
    slug = models.SlugField('Identificador', max_length=100)
    # data de adição
    created = models.DateTimeField('Criado em', auto_now_add=True)
    # data de modificação
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        # ordernar alfabeticamente por nome
        ordering = ['name']

    # Representar o objeto como string para melhorar sua visualização no ADMIN
    def __str__(self):
        return self.name
    
    # O próprio modelo sabe qual é a sua url de acesso.
    def get_absolute_url(self):
        return reverse('catalog:products', kwargs={'slug': self.slug})


class Products(models.Model):

    # nome do produto
    name = models.CharField('Nome', max_length=30)
    # slug
    slug = models.SlugField('Identificador', max_length=30)
    # categoria do produto
    category = models.ForeignKey('catalog.Category', on_delete= models.CASCADE, verbose_name='Categoria' )
    # descrição do produto
    description = models.TextField('Descrição', blank=True)
    # quantidade do produto
    quantity = models.PositiveIntegerField('Quantidade', )
    # preço do produto
    price = models.DecimalField('Preço',max_digits=7, decimal_places=2)
    # imagem do produto
    # data de adição do produtos ao estoque
    created = models.DateTimeField('Criado em',auto_now_add=True)
    # data de modificação do produto no estoque
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    # Representar o objeto como string para melhorar sua visualização no ADMIN
    def __str__(self):
        return self.name
    
    def product_detail_url(self):
        return reverse('catalog:product_detail', kwargs={'slug': self.slug})
    """
    def lowest_prices(self):
        low_price_list = Products.objects.order_by('price')
        return low_price_list
    """