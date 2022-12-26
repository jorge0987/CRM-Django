from django.shortcuts import get_object_or_404, redirect, render

from .models import clients, company, companyowner, product, transations


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product_new.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})


def transations_list(request):
    transations = transations.objects.all()
    return render(request, 'transations', {'transations': transations})


def transations_new(request):
    if request.method == 'POST':
        form = transationsForm(request.POST)
        if form.is_valid():
            transations = form.save()
            return redirect('transations_detail', pk=transations.pk)
    else:
        form = transationsForm()
    return render(request, 'transations_new.html', {'form': form})


def transations_edit(request, pk):
    transations = get_object_or_404(transations, pk=pk)
    if request.method == 'POST':
        form = transationsForm(request.POST, instance=transations)
        if form.is_valid():
            transations = form.save()
            return redirect('transations_detail', pk=transations.pk)
    else:
        form = transationsForm(instance=transations)
    return render(request, 'transations_edit.html', {'form': form})


def transations_delete(request, pk):
    transations = get_object_or_404(transations, pk=pk)
    if request.method == 'POST':
        transations.delete()
        return redirect('transations_list')
    return render(request, 'transations_delete.html', {'transations': transations})


def makesale_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            return redirect('transaction_detail', pk=transaction.pk)
    else:
        form = TransactionForm()
    return render(request, 'make_transaction.html', {'form': form})


def liststock(request):
    products = Product.objects.all()
    return render(request, 'liststock.html', {'products': products})


def displaybilling(request):
    transactions = Transaction.objects.invoicing()
    return render(request, 'displaybilling.html', {'transactions': transactions})
