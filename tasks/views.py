from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from tasks import models, forms

#Listagem de Tarefas (Página Inicial)
class Index(LoginRequiredMixin, generic.ListView):
    model=models.Task
    context_object_name='tasks'
    template_name='tasks/index.html'
    paginate_by=5

    def get_queryset(self):
        return models.Task.objects.filter(usuario=self.request.user)


#Visualização de Tarefa
class Task(LoginRequiredMixin, generic.DetailView):
    model=models.Task
    context_object_name='task'
    template_name='tasks/task.html'

#Criação de Nova Tarefa
class Create(LoginRequiredMixin, generic.CreateView):
    form_class=forms.FormTask
    context_object_name='form'
    template_name='tasks/form.html'
    success_url=reverse_lazy('tasks:Index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

#Atualização de Tarefa
class Update(LoginRequiredMixin, generic.UpdateView):
    model=models.Task
    form_class=forms.FormTask
    context_object_name='form'
    template_name='tasks/update.html'
    success_url=reverse_lazy('tasks:Index')

#Deletar Tarefa
class Delete(LoginRequiredMixin, generic.DeleteView):
    model=models.Task
    context_object_name='task'
    template_name='tasks/delete.html'
    success_url=reverse_lazy('tasks:Index')

#Inserir Data de Conclusão
class Complete(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        task = get_object_or_404(models.Task, pk=pk)
        task.mark_as_completed()
        return redirect('tasks:Index')