from django.shortcuts import render

import random
import time

# Create your views here.
quotes = [
    "I would like to die on Mars. Just not on impact.",
    "Rockets are cool. There's no getting around that.",
    "When something is important enough, you do it even if the odds are not in your favor.",
    "It's OK to have your eggs in one basket as long as you control what happens to that basket.",
    "I've actually not read any books on time management.",
    "I think it is possible for ordinary people to choose to be extraordinary.",
    "I could either watch it happen or be a part of it.",
]

images = [
    "https://upload.wikimedia.org/wikipedia/commons/c/cb/Elon_Musk_Royal_Society_crop.jpg",
    "https://www.investopedia.com/thmb/XJDLdvCuNbcWk_EVZzXx84ae82c=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1258889149-1f50bb87f9d54dca87813923f12ac94b.jpg",
    "https://media.cnn.com/api/v1/images/stellar/prod/c-2025-01-29t200958z-751044450-rc2qdca4cgkl-rtrmadp-3-tesla-results.jpg?c=16x9&q=h_833,w_1480,c_fill",
    "https://hips.hearstapps.com/hmg-prod/images/elon-musk-gettyimages-2147789844-web-675b2c17301ea.jpg?crop=0.6666666666666666xw:1xh;center,top&resize=640:*",
    "https://media.cnn.com/api/v1/images/stellar/prod/221027200356-elon-musk-twitter-pba.jpg?c=original",
    "https://fortune.com/img-assets/wp-content/uploads/2020/11/BPO01.21.gettyimages-1183851343-2048x2048-1.jpg?w=1440&q=75",
]

last_quote = None

def quote(request):
    global last_quote

    new_quote = random.choice(quotes)

    while new_quote == last_quote:
        new_quote = random.choice(quotes)
    last_quote = new_quote

    template_name = 'quotes/quote.html'
    context = {
        'quote': new_quote,
        'image': random.choice(images),
        'time': time.ctime(),
    }
    return render(request, template_name, context)

def show_all(request):
    template_name = 'quotes/show_all.html'
    context = {
        'quotes': quotes,
        'images': images,
        'time': time.ctime(),
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'quotes/about.html'
    context = {
        'quotes': quotes,
        'images': images,
        'time': time.ctime(),
    }
    return render(request, template_name, context)