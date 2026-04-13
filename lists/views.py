from django.shortcuts import render  # <--- ESSA LINHA É OBRIGATÓRIA

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })