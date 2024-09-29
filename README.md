# DjangoWebScraper
This project is a web scraper app created in Django.

To view project, extract contents of the repository to a folder and open folder in IDE of your choice. Then in the IDE terminal, "cd" to the folder containing the project and use the command "python manage.py runserver". Then you can access the blog through your internet browser by typing in the URL http://127.0.0.1:8000/.

To specify a website to scrape, open scraper\views.py and modify url link in the scrape_website(request) function. 'https://www.wikipedia.org/' has been used as an example.
To specify what section of a website to scrape, open scraper\views.py and modify the argument for headlines = soup.find_all in the response.status_code if statement. 'h1' has been used as an example.


!IMPORTANT! Make sure Django is installed prior to accessing the server.

Contributing Feel free to fork the repository and submit pull requests for improvements or bug fixes.

License This project is licensed under the MIT License.
