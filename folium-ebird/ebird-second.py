import ebird.api as eb
from pprint import pprint

apiKey = "kd6mhl9s6m9c"

countyNameToRecords = {}

# Getting a list of dictionaries, each of which describes a county in MA.
#   Each dictionary contains a county's code (ID) and name. 
#   "subnational2" means counties.
counties = eb.get_regions(apiKey, "subnational2", "US-MA")
# pprint(counties)
    # US-MA-017 is the code for Middlesex conty

for county in counties:
    countyCode = county["code"]
    countyName = county["name"]
    records = eb.get_observations(apiKey, countyCode, back=7)
#     pprint(records)
#     print(f"{len(records)} spieces observed in {countyName} county.")

    totalObsCount = 0
    for r in records:
        if "howMany" not in r: r["howMany"] = 1
        totalObsCount += r["howMany"]
    print(f"{totalObsCount} observations in {countyName} county")

    recordsSortedByObsCount = sorted(records, key = lambda listElem:listElem["howMany"], reverse=True)
#     for i in range(5):
#         print("   ", recordsSortedByObsCount[i]["comName"], recordsSortedByObsCount[i]["howMany"])
    countyNameToRecords[countyName] = {}
    countyNameToRecords[countyName]["records"] = recordsSortedByObsCount
    countyNameToRecords[countyName]["totalObsCount"] = totalObsCount

for item in countyNameToRecords.items():
    print( item[1]["totalObsCount"] )


# countyNameToRecordsSortedByTotalObsCount = sorted(countyNameToRecords,
#                                                   key = lambda dictItem: dictItem[1]["totalObsCount"],
#                                                   reverse=True)



# for countyName, countyData in enumerate(countyNameToRecordsSortedByTotalObsCount.items()):
#     print(f"{countyName}, {countyData['totalObsCount']} observations")

