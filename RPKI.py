from RipeRouteAnnounced import RouteAnnounced
import requests
ripe = RouteAnnounced()

sp1 = ripe.ripe_route_announced()
for routes in range(len(sp1)):
    print("Route Annonced : {} ".format(sp1[routes]))
print("\n\n")
for JustPrefixes in range(len(sp1)):
    result = sp1[JustPrefixes]
    url = "https://stat.ripe.net/data/rpki-validation/data.json?resource=49666&prefix={}".format(result)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    checkrpki = response.json()
    PREFIX_VALIDATION = checkrpki["data"]["validating_roas"]
    # print(PREFIX_VALIDATION)
    for checkvalidation in range(len(PREFIX_VALIDATION)):
        PREFIX_EX = PREFIX_VALIDATION[checkvalidation]["prefix"]
        VALIDITY = PREFIX_VALIDATION[checkvalidation]["validity"]
        if VALIDITY == "valid":
            print("prefix is {} and validity is {}".format(PREFIX_EX, VALIDITY))
        else:
            print("prefix {} Should be checked ---> {}".format(PREFIX_EX, VALIDITY))
    print()
