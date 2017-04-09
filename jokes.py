import requests
from bs4 import BeautifulSoup

def scrape():

    url = "http://123hindijokes.com/very-funny-jokes/"

    code = requests.get(url)
    soup = BeautifulSoup(code.content, "lxml")
    text = soup.findAll('ul', {'class': 'statusList'})

    f = open('jokes.html', 'w')

    html = """
<!DOCTYPE html>
<html>
<head>
 	<meta charset="utf-8">
	<title>Scraped Hindi Jokes</title>
</head>
<body>
<h1>Python Web Scraping</h1>
<p>Scraped from: <a href="http://123hindijokes.com/very-funny-jokes/">http://123hindijokes.com/very-funny-jokes/</a></p>
<p>
    """
    html += str(text)[1:-1]
    html += """
</p>
</body>
</html>
    """

    f.write(html)
    f.close()
    print("Success!")   

scrape()
