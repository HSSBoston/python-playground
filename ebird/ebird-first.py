from ebird.api import get_observations
from pprint import pprint

apiKey = "kd6mhl9s6m9c"

# Get observations from Woodman Pond, Madison county, New York for the past week.
records = get_observations(apiKey, 'L227544', back=7)
pprint(records)

# 
# # Get observations from Madison county, New York
# records = get_observations(api_key, 'US-NY-053')
# 
# # Get observations from New York
# records = get_observations(api_key, 'US-NY')
# 
# # Get observations from the USA - don't overdo the data downloads
# records = get_observations(api_key, 'US')