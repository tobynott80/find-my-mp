import requests



#if __name__ == "__main__":
if False:
    url = "https://members-api.parliament.uk/api/Location/Constituency/Search?searchText="+ search
    search = str(input("Enter PostCode or other search term: "))
    resp = requests.get(url)

    print("Searching")

    if resp.status_code == 200: 
        print("Done!")
        data = resp.json()
        if data["totalResults"] == 0:
            print("No results found")
        print(data["resultContext"])
        firstRes = (data["items"][0]["value"])
        mp = firstRes["currentRepresentation"]["member"]["value"]
        print("Your constituancy is {}".format(firstRes["name"]))
        print("Your MP is {}".format(mp["nameDisplayAs"]))
        print("Your MP belongs to the {} party".format(mp["latestParty"]["name"]))

def searchMP(query): #searches for mp and returns ID
    url = "https://members-api.parliament.uk/api/Location/Constituency/Search?searchText="+ query
    resp = requests.get(url)
    data = resp.json()
    if resp.status_code == 200:
        if data["totalResults"] == 0:
            return "Not Found"
        else:
            return data["items"][0]["value"]["id"]
    else:
        return 400
    


mpID = searchMP("cf143uu")

