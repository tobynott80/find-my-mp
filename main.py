import requests


search = str(input("Enter PostCode or other search term: "))
url = "https://members-api.parliament.uk/api/Location/Constituency/Search?searchText="+ search


resp = requests.get(url)

print("Searching")

if resp.status_code == 200:
    print("Done!")
    data = resp.json()
    print(data["resultContext"])
    firstRes = (data["items"][0]["value"])
    mp = firstRes["currentRepresentation"]["member"]["value"]
    print("Your constituancy is {}".format(firstRes["name"]))
    print("Your MP is {}".format(mp["nameDisplayAs"]))
    print("Your MP belongs to the {} party".format(mp["latestParty"]["name"]))


    