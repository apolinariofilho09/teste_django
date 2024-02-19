from django import forms
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Submit, Row, Column
from tasks import models

class FormTask(forms.ModelForm):
    class Meta:
        model=models.Task
        fields='__all__'
        labels={
            'text_description': 'Descrição da Tarefa',
            'date_delivery':'Previsão de Entrega (dd/mm/yyyy)',
            'date_complete': 'Data de Conclusão (dd/mm/yyyy)'
        }
    
    def clean_date_delivery(self):
        date_delivery = self.cleaned_data['date_delivery']
        if date_delivery.date() < timezone.now().date():
            raise forms.ValidationError('A Previsão de Entrega Precisar ser Maior ou Igual a Hoje!')
        return date_delivery

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('text_description', css_class='form-group col-md-5 mb-0'),
                Column('date_delivery', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('date_complete', css_class='form-group col-md-5 mb-0'),
                #Column('usuario', css_class='form-group col-md-5 mb-0'),
            ),
            Submit('submit', 'Salvar'),
            HTML('<a href="{% url "tasks:Index" %}" class="btn btn-danger">Cancelar</a>')
        )