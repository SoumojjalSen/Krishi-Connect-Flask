import requests


api_key = '579b464db66ec23bdd000001420beab8b9a546d268d7c574c638dbe3'

api_url = 'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070'


def fetch_data(state):
    params = {
        'api-key': api_key,
        'format': 'json',
        'filters[state]': state,
        'limit':2000
    }

    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            return data
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return None


def display_district_data(data):
    if data:
        
        final = []
        for record in data['records']:
            market_data={}
            market_data["state"] = record['state']
            market_data["District:"] = record['district']
            market_data["Market:"] = record['market']
            market_data["Commodity:"] = record['commodity']
            market_data["Variety:"] = record['variety']
            market_data["Grade:"] = record['grade']
            market_data["Arrival Date:"] = record['arrival_date']
            market_data["Min Price:"] = record['min_price']
            market_data["Max Price:"] = record['max_price']
            market_data["Modal Price:"] = record['modal_price']
            final.append(market_data)
        return final
    return None

def market_data(state):
    data = fetch_data(state)

    if data:
        return display_district_data(data)
    else:
        return None
