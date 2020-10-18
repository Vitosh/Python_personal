from django.shortcuts import render


def show_info(request):
    context = {
        'some_title': 'vitoshacademy.com INFO',
        'info_info': 'The site is available at https://vitoshacademy.com',
    }
    return render(request, 'vitoshacademy/info.html', context)


def show_about(request):
    context = {
        'some_title': 'vitoshacademy.com ABOUT',
        'info_about': 'We can talk about vitoshacademy.com a lot!',
    }
    return render(request, 'vitoshacademy/about.html', context)
