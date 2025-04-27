from django.shortcuts import render, redirect
from .models import BlogPost
from .models import Contact
from .models import Recipe

def base_test(request):
    return render(request, 'recettes/base.html')
def about_page(request):
    return render(request, 'recettes/about.html')
def element_page(request):
    return render(request, 'recettes/elements.html')
def blog_page(request):
    return render(request, 'recettes/blog-post.html')
def blog_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'recettes/blog-post.html', {'posts': posts})
from django.shortcuts import render, redirect
from .models import Contact

def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Sauvegarder dans la base
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        return redirect('contact')  # ou affiche un message de succès

    return render(request, 'recettes/contact.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recettes/receipe-post.html', {'recipes': recipes})

def recipe_list(request):
    recipes = Recipe.objects.all()
    for recipe in recipes:
        recipe.ingredients_list = recipe.ingredients.split(',')
    return render(request, 'recettes/receipe-post.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recettes/recipe_detail.html', {'recipe': recipe})