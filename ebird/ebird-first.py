from ebird.api import get_observations

# Get observations from Woodman Pond, Madison county, New York for the past week.
records = get_observations(api_key, 'L227544', back=7)

# Get observations from Madison county, New York
records = get_observations(api_key, 'US-NY-053')

# Get observations from New York
records = get_observations(api_key, 'US-NY')

# Get observations from the USA - don't overdo the data downloads
records = get_observations(api_key, 'US')