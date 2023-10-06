from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . forms import todoform
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'results'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'detail'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'edit'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs = {'pk': self.object.id})
class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home.html')
def add(request):
    variable=Task.objects.all()
    if request.method=='POST':
        variable1=request.POST.get('task','')
        variable2=request.POST.get('priority','')
        variable3=request.POST.get('date','')
        user=Task(a=variable1, b=variable2, c=variable3)
        user.save()
    return render(request,'home.html',{"results":variable})
# def details(request):
#
#     return render(request,'details.html',)
def delete(request,id):
    variablee=Task.objects.get(id=id)
    if request.method=='POST':
        variablee.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    task1=todoform(request.POST or None,instance=task)
    if task1.is_valid():
        task1.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'task1':task1})