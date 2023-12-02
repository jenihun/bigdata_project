import googlemaps

def get_lat_lon_from_country(country_name):
    # Initialize the Google Maps API client
    gmaps = googlemaps.Client(key='AIzaSyDMamPU-7XvWudTvCJwjb27mk1_uL7R6T8')

    # Geocode the country
    geocode_result = gmaps.geocode(country_name, language='ko')

    if geocode_result:
        # Extract necessary information
        formatted_address = geocode_result[0]['formatted_address']
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']

        return {
            'name': formatted_address,
            'lat': latitude,
            'lng': longitude
        }
    else:
        return None
