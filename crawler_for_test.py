import requests
import re

url = "http://www.revistabula.com/7073-a-lista-definitiva-dos-100-melhores-filmes-de-todos-os-tempos/"
url2 = "https://www.nba.com/stats/players/traditional"
check = []

r = requests.get(url2)
html = r.text
search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html)

for link in search:
    if link not in check:
        check.append(link)
        # for your own test, you can replace it "link2" to a word of your choice
        with open("link2.txt", "a") as file:
            file.write(f'{link}\n')
