from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

# Create your views here.
'''
def index(request):
    return(render(request,'otomne/index.html'))
    #return HttpResponse("Hello, world. You're at the polls index.")
'''

def index(request):
    import math
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            # print (form.cleaned_data['your_name'])
            # ...
            your_name = form.cleaned_data['your_name']
            out = str('Vous venez de saisir : %s' %your_name)
            len_out = str('La longueur de votre saisie est : %d' %len(your_name))
            a = float(math.cos(45))
            des_maths= str('Le cosinus de 45 vaut : %f' %a)
            #print('La longueur est %d' %length)
            #return HttpResponse('Vous venez de taper votre nom %s' %your_name)
            args = {'form': form, 'out': out, 'len_out' : len_out, 'des_maths': des_maths}
            return render(request, 'otomne/index.html', args)
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()

        return render(request, 'otomne/index.html', {'form': form})
