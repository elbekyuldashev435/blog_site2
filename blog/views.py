from django.shortcuts import render, redirect,  get_object_or_404
from django.views import View
from .models import Products, Saved, About, Comments
from .forms import ProductUpdateForm, AddCommentForm
# Create your views here.


class AboutView(View):
    def get(self, request):
        about1 = About.objects.all()
        context = {
            'about_us': about1
        }
        return render(request, 'about.html', context=context)


class ProductsView(View):
    def get(self, request):
        products = Products.objects.all()
        context = {
            'products': products
        }
        return render(request, 'home.html', context=context)


class DetailView(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        context = {
            'product': product,

        }
        return render(request, 'detail.html', context=context)


class ProductUpdate(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        update_form = ProductUpdateForm(instance=product)
        context = {
            'form': update_form
        }
        return render(request, 'product_update.html', context=context)

    def post(self, request, pk):
        product = Products.objects.get(pk=pk)
        update_form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if update_form.is_valid():
            update_form.save()
            return redirect('home:detail', pk=pk)
        else:
            context = {
                'form': update_form
            }
            return render(request, 'product_update.html', context=context)
class SavedView(View):
    def get(self, request):
        # Display saved products for the user
        saved_items = Saved.objects.filter(user=request.user).select_related('product')
        return render(request, 'saved.html', {'saved_items': saved_items})

    def post(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        if not Saved.objects.filter(product=product, user=request.user).exists():
            Saved.objects.create(product=product, user=request.user)
        return redirect('home:saved')


class AddCommentView(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        comment_form = AddCommentForm()
        context = {
            'product': product,
            'form': comment_form
        }
        return render(request, 'add_comment.html', context=context)

    def post(self, request, pk):
        product = Products.objects.get(pk=pk)
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
            return redirect('home:detail', pk=pk)
        else:
            context = {
                'product': product,
                'form': comment_form
            }
            return render(request, 'add_comment.html', context=context)

class CommentView(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        comments = Comments.objects.filter(product=pk)
        context = {
            'product': product,
            'comments': comments
        }
        return render(request, 'comments.html', context=context)