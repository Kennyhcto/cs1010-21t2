import requests

# API used: https://rapidapi.com/apidojo/api/imdb8/

if __name__ == "__main__":
    url = "https://imdb8.p.rapidapi.com/auto-complete"

    querystring = {"q":"game of thr"}

    headers = {
        'x-rapidapi-key': "d59782ca6amsh91cbab006569dfap1e69d9jsn3ad1e49d6ad4",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)