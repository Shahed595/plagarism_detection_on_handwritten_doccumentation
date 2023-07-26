from django.shortcuts import render,redirect
from paper.forms import PaperStoreForm
from paper.models import PaperStoreModel

# Create your views here.
def home(request):
    return render(request, 'home.html')

def store_paper(request):
    if request.method == 'POST':
        paper_store = PaperStoreForm(request.POST)
        if paper_store.is_valid():
            paper_store.save()
            # print(paper_store.cleaned_data)
            return redirect('show_papers')
    else:
        paper_store = PaperStoreForm()
    return render(request, 'store_paper.html', {'form':paper_store})

def show_papers(request):
    paper = PaperStoreModel.objects.all()
    print(paper)
    return render(request, 'show_paper.html', {'data' : paper})

def edit_book(request,id):
    paper = PaperStoreModel.objects.get(pk=id)
    form = PaperStoreForm(instance=paper)
    if request.method == 'POST':
        form = PaperStoreForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return redirect('show_papers')
    return render(request,'store_paper.html', {'form':form})

def delete_paper(request,id):
    paper = PaperStoreModel.objects.get(pk=id).delete()
    return redirect('show_papers')
    
    