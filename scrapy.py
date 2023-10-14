import requests
import csv

# Replace with your RapidAPI endpoint URL
endpoint_url = 'https://google-reviews-scraper.p.rapidapi.com/'

# Replace with your RapidAPI key
api_key = '5734613431msh899da255b1f1548p184441jsna8df727a0eea'

querystring = {
    "fullid": "U2FsdGVkX19p%2B1Ag0p7RQaQcHERht%2FC5gUCYBW19QD42AJFQs8NzSIwnHGnOKgHm5yw75q8nDULs3FrfkJRkYw%3D%3D",
    "fullsort": "relevant"
}

# Specify the location or query for which you want to scrape reviews
location = "Fire and Ice Pizzeria"

# Set the headers with your API key
headers = {
    'X-RapidAPI-Host': 'google-reviews-scraper.p.rapidapi.com',
    'X-RapidAPI-Key': api_key,
}

# Make a request to the RapidAPI endpoint
params = {
    'query': location,
    'num_reviews': 10  # You can adjust the number of reviews you want to scrape
}
response = requests.get(endpoint_url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()

    # Extract and save the reviews to a CSV file
    reviews = data.get('reviews', [])

    with open('google_reviews2.csv', 'w', newline='') as csv_file:
        fieldnames = ['author', 'rating', 'comment', 'date']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for review in reviews:
            author = review.get('author', 'N/A')
            rating = review.get('rating', 'N/A')
            comment = review.get('comment', 'N/A')
            date = review.get('date', 'N/A')

            # Extract the numeric rating from the "rating" field
            rating = rating.split('Rated ')[1].split(' out of')[0]

            writer.writerow({
                'author': author,
                'rating': rating,
                'comment': comment,
                'date': date
            })

    print("Reviews saved to google_reviews.csv")
else:
    print(f"Error: {response.status_code} - {response.text}")
