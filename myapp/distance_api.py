import requests


class DistanceMatrixAPI:

    def __int__(self):
        self.params = {
            "key": "AIzaSyBeBsBzLYbb6-GEY_pMFjwcYpTXTQTO0YU",
        }
        self.base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    def get_distance_matrix(self, origin, destination=None, lat_long=None, place_id=None):
        des = None
        if place_id:
            des = place_id
        elif destination:
            des = destination

        params = {
            "key": "AIzaSyBeBsBzLYbb6-GEY_pMFjwcYpTXTQTO0YU",
            "origins": origin,
            "destinations": des if des else lat_long
        }
        payload = {}
        headers = {
            'Accept': 'application/json'
        }
        response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=params, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()
