country = input("enter country: ")
visits = int(input("number of visits: "))
listOfCities = eval(input("Enter list of cities: "))

travelLog = [
    {
     "country": "France", 
     "visits": 12,
     "cities": ["Paris","Lillie", "Dijon"]
     },
    {
     "country": "Germany",
     "visits": 5,
     "cities": ["Berlin", "Hamburg","Stuttgart"]
     }
]

def addNewCountry(country, visits, listOfCities):
    newEntry = {"country": country,
                "visits": visits,
                "cities": listOfCities}
    
    travelLog.append(newEntry)

addNewCountry(country, visits, listOfCities)
print(f"\nI've been to {travelLog[2]['country']} {travelLog[2]['visits']} times.")
print(f"My favourite city was {travelLog[2]['cities'][0]}.")
