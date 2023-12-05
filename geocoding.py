import json
import googlemaps

def get_lat_lon_from_country(country_name):
    # Initialize the Google Maps API client
    gmaps = googlemaps.Client(key='API키 입력')

    # Geocode the country
    geocode_result = gmaps.geocode(country_name, language='ko')

    if geocode_result:
        # Extract necessary information
        formatted_address = geocode_result[0]['formatted_address']
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']

        # Create a dictionary with the extracted information
        data = {
            'name': formatted_address,
            'lat': latitude,
            'lng': longitude
        }

        return data
    else:
        return None

# Example usage
countries = [
    'United Kingdom', 'France', 'Germany', 'Italy', 'Spain',
    'Ireland', 'Portugal', 'Belgium', 'Netherlands', 'Denmark',
    'Norway', 'Sweden', 'Finland', 'Poland', 'Czech Republic',
    'Austria', 'Croatia', 'Slovakia', 'Hungary', 'Serbia',
    'Greece', 'Lithuania', 'Estonia', 'Latvia', 'Belarus',
    'Ukraine', 'Romania', 'Bulgaria', 'Moldova', 'Korea',
    'Saudi Arabia', 'Japan', 'Philippines', 'Singapore', 'Indonesia',
    'India', 'China', 'Mongolia', 'Myanmar', 'Laos',
    'Bhutan', 'Bangladesh', 'Nepal', 'Sri Lanka', 'Pakistan',
    'Kyrgyzstan', 'Australia', 'Russia', 'Tajikistan', 'Kazakhstan',
    'Uzbekistan', 'Turkmenistan', 'Iran', 'Oman', 'United Arab Emirates',
    'Kuwait', 'Iraq', 'Yemen', 'Azerbaijan', 'Georgia',
    'Turkey', 'Jordan', 'Israel', 'Lebanon', 'Syria',
    'Egypt', 'Sudan', 'Eritrea', 'Djibouti', 'Ethiopia',
    'Somalia', 'Kenya', 'Uganda', 'Tanzania', 'Malawi',
    'Mozambique', 'Zimbabwe', 'Zambia', 'Botswana', 'South Africa',
    'Namibia', 'Angola', 'Democratic Republic of the Congo', 'Central African Republic', 'Gabon',
    'Cameroon', 'Nigeria', 'Benin', 'Niger', 'Chad',
    'Mali', 'Togo', "Côte d'Ivoire", 'Liberia', 'Sierra Leone',
    'Guinea', 'Senegal', 'Mauritania', 'Western Sahara', 'Algeria',
    'Tunisia', 'Madagascar', 'United States', 'Canada', 'Mexico',
    'Argentina', 'Brazil', 'Colombia', 'Peru', 'Bolivia',
    'Uruguay', 'Paraguay', 'Chile', 'Puerto Rico', 'Cuba',
    'Suriname', 'Venezuela'
]
