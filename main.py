import requests


def searchMP(query): #searches for mp and returns ID
    url = "https://members-api.parliament.uk/api/Location/Constituency/Search?searchText="+ query
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code == 200:
        if data["totalResults"] == 0:
            return 0
        else:
            return str(data["items"][0]["value"]["currentRepresentation"]["member"]["value"]["id"])
    else:
        return 400
    
def mpDetails(mpID):
    url = "https://members-api.parliament.uk/api/Members/" + mpID
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        return data
    else:
        return "Not found"
    

if __name__ == "__main__":
    search = str(input("Enter PostCode or other search term: "))
    mpID = searchMP(search)
    if mpID == 0:
        print("Not found")
    else:
        data = mpDetails(mpID)
        print("Your constituancy is {}".format(data["value"]["latestHouseMembership"]["membershipFrom"]))
        print("Your MP is {}".format(data["value"]["nameFullTitle"]))
        print("Your MP belongs to the {} party".format(data["value"]["latestParty"]["name"]))
