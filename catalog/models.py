from django.db import models


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