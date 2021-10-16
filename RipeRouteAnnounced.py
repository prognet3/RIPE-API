import requests
import datetime as dt


class RouteAnnounced:
    def ripe_route_announced(self):
        time_update = dt.datetime.now().date()
        url = "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS49666&starttime={}T12:00".format(
            time_update)
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        # print(response.json())
        changetojson = response.json()
        # print(type(ChangeToJson))
        prefixeslist = changetojson['data']['prefixes']
        finalprefixes = []
        for JustPrefixes in range(len(prefixeslist)):
            result = prefixeslist[JustPrefixes]['prefix']
            finalprefixes.append(result)
        return finalprefixes
