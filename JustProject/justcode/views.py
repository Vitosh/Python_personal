from django.shortcuts import render


def show_vba(request):
    context = {
        'some_title': 'VBA Information',
        'info_vba': 'VBA is not a macro!',
    }
    return render(request, 'justcode/vba.html', context)


def show_python(request):
    context = {
        'some_title': 'Python Information',
        'info_python': 'Python is a Dutch snake!',
    }
    return render(request, 'justcode/python.html', context)
