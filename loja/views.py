from django.views.generic import ListView, DetailView, TemplateView
from loja.models import Categoria, Produto


class IndexView(TemplateView):
    template_name = 'loja/index.html'

class ProdutoListView(ListView):
    template_name = 'loja/produtos/listar.html'
    model = Produto
    queryset = Produto.disponiveis.all()
    context_object_name = 'produtos'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        categoria = None
        categorias = Categoria.objects.all()
        if self.kwargs and self.kwargs['categ_slug']:
            slug = self.kwargs['categ_slug']
            categoria = Categoria.objects.get(slug=slug)
        contexto['categoria'] = categoria
        contexto['categorias'] = categorias
        return contexto

    def get_queryset(self):
        qs = super().get_queryset()
        if self.kwargs and self.kwargs['categ_slug']:
            slug = self.kwargs['categ_slug']
            categoria = Categoria.objects.get(slug=slug)
            return qs.filter(categoria=categoria)
        return qs
class ProdutoDetailView(DetailView):
    template_name = 'loja/produtos/detalhe.html'
    model = Produto
