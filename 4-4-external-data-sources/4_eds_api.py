import requests

# API used: https://rapidapi.com/apidojo/api/imdb8/

if __name__ == "__main__":
    url = "https://imdb8.p.rapidapi.com/title/get-coming-soon-movies"

    querystring = {"homeCountry":"US","purchaseCountry":"US","currentCountry":"AU"}

    headers = {
        'x-rapidapi-key': "d59782ca6amsh91cbab006569dfap1e69d9jsn3ad1e49d6ad4",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    coming_soon_response = requests.request("GET", url, headers=headers, params=querystring)

    count = 0
    for title in coming_soon_response.json():
        #print(title[7:16])
        url = "https://imdb8.p.rapidapi.com/title/get-details"
        querystring = {"tconst":title[7:16]}
        details_response = requests.request("GET", url, headers=headers, params=querystring)

        info = details_response.json()
        print(info['titleType']+": "+info['title'])
        count += 1
        if count == 20:
            break