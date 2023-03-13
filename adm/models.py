from django.db import models
from stdimage.models import StdImageField
from django.template.defaultfilters import slugify
from django.db.models import signals

class Gerenciador(models.Model):
    nome = models.CharField('Nome', max_length=150)
    idade = models.IntegerField('Idade')
    email = models.EmailField('Email', max_length=120)
    cpf = models.CharField('CPF', max_length=15)

    def __str__(self):
        return self.nome.capitalize().strip()

class Receita(models.Model):
    tipo_receita = models.CharField('Informe qual o tipo de receita', max_length=8)
    valor = models.DecimalField('Informe o valor', max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.tipo_receita.title().strip()} R${self.valor}'

class Solicitacoes(models.Model):
    titulo = models.CharField('Titulo da solicitação', max_length=75)
    conteudo = models.CharField('Conteudo da solicitação', max_length=125)
    adm = models.ForeignKey(Gerenciador, on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class CategoriaProduto(models.Model):
    nome_categoria = models.CharField('Nome da categoria',max_length=25)

    def __str__(self):
        return self.nome_categoria

class Produto(models.Model):
    nome_produto = models.CharField('Nome do produto', max_length=150)
    preco_unitario = models.DecimalField('Preço unitario', max_digits=6, decimal_places=2)
    estoque = models.IntegerField('Estoque disponivel')
    imagem = StdImageField('Imagem do produto', upload_to='produto', variations={'thumb': {'width': 450, 'height': 300, 'crop': True}})
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.CASCADE, default='')
    postado_por = models.ForeignKey(Gerenciador, on_delete=models.CASCADE)
    slug = models.SlugField('Slug', editable=False, unique=True, blank=True)

    def __str__(self):
        return self.nome_produto

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome_produto)

signals.pre_save.connect(produto_pre_save, sender=Produto)

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField('Quantidade')
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.produto}'