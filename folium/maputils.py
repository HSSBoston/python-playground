from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="spaceapps24")

# Takes "cityName, stateCode" as cityState and returns its (lat, lon).
#
def cityStateToLatLon(cityState):
    queryParams = {"city" : cityState.split(",")[0].lstrip().rstrip(),
                   "state" : cityState.split(",")[1].lstrip().rstrip(),
                   "country" : "United States" }
    location = geolocator.geocode(query=queryParams, timeout=1000)
    if location != None:
        return (location.latitude, location.longitude)
    else:
        raise RuntimeError(f"Failed to find (lat, lon) for {cityState}.")




if __name__ == "__main__":
    print( cityStateToLatLon("Boston, MA") )
    waCities = ["Seattle, WA", "Bellevue, WA", "Renton, WA", "Issaquah, WA", "North Bend, WA",
                "Easton, WA", "Cle Elum, WA", "Quincy, WA", "George, WA", "Ritzville, WA",
                "Ellensburg, WA", "Sprague, WA", "Cheney, WA", "Spokane, WA", "Liberty Cake, WA"]
    for city in waCities:
        print( city, cityStateToLatLon(city) )
    
