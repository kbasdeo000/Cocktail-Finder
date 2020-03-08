import requests

url = "https://the-cocktail-db.p.rapidapi.com/list.php"

querystring = {"a":"list"}

headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "d26e151dcfmsh3cfe89b384bcf04p1831bdjsn7096b3296f6c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


print(response.json())


