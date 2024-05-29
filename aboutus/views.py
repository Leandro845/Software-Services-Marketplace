from django.shortcuts import render

# View for rendering the 'about' page
def about(request):
    return render(request, 'about.html')

# View for rendering the 'click' page
def click(request):
    return render(request, 'click.html')

# View for rendering the 'wedo' page
def wedo(request):
    return render(request, 'wedo.html')
