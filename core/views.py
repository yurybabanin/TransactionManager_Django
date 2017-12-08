from django.shortcuts import render, get_object_or_404, redirect
from .models import Transactions
from .forms import PostFrom


def post_list(request):
    trans = Transactions.objects.order_by('id')
    return render(request, 'core/post_list.html', {'trans': trans})

def show_cur_tran(request, id):
    trans = get_object_or_404(Transactions ,id = id)
    return render(request, 'core/show.html', {'trans': trans})

def tran_new(request):
    if request.method == "POST":
        form = PostFrom(request.POST)
        if form.is_valid():
            tran = form.save(commit=False)
            tran.save()
            return redirect('show', id=tran.id)
    else:
        form = PostFrom()
    return render(request, 'core/tran_new.html', {'form' : form})