from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse

def scrape_website(request):
    url = 'https://www.wikipedia.org/'  # Replace with the website you want to scrape
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example: Extract all headlines from <h2> tags
        headlines = soup.find_all('h1')
        results = [headline.get_text() for headline in headlines]

        return JsonResponse({'headlines': results})
    else:
        return JsonResponse({'error': 'Failed to retrieve the webpage'}, status=400)

