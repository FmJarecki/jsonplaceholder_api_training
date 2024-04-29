import requests
from config import API_KEY


def get_data_from_api(url: str, params=None) -> list:
    if params is None:
        params = []
    api_url = f"{url}?{'&'.join([f'{param[0]}={param[1]}' for param in params])}"
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        response_dict = response.json()
        if isinstance(response_dict, dict):
            return [response_dict]
        return response_dict
    else:
        # print("Error:", response.status_code, response.text)
        return []


class Person:
    def __init__(self, person_data: dict):
        self._name: str = self._set_name(person_data['name'])
        self._email: str = self._set_email(person_data['company']['name'])
        self._lng, self._lat = person_data['address']['geo']['lng'], person_data['address']['geo']['lat']
        self._city: str = self.find_city()
        self._country: str = self.find_country()
        
    def __str__(self):
        return f'name: {self._name}, email: {self._email}, city: {self._city}, country: {self._country}'

    def _set_name(self, name_data: str) -> str:
        if '.' in name_data.split(' ')[0]:
            name_data = name_data.split(' ', 1)[1].strip()
        return name_data

    def _set_email(self, company_name: str) -> str:
        words = self._name.split(" ")
        name_part = words[0] + '.' + ''.join(words[1:])
        address_part = ''.join(char for char in company_name if char.isalpha())
        return f'{name_part}@{address_part}'

    def find_country(self) -> str:
        params = [
            ["lat", self._lat],
            ["lon", self._lng],
            ['format', 'json']
        ]
        api_url = 'https://nominatim.openstreetmap.org/reverse'
        continent_data = get_data_from_api(api_url, params)
        if 'address' in continent_data[0]:
            return continent_data[0]['address']['country']
        else:
            return 'No country found.'

    def find_city(self) -> str:
        params = [
            ["lat", self._lat],
            ["lon", self._lng]
        ]
        api_url = 'https://api.api-ninjas.com/v1/reversegeocoding'
        city_data = get_data_from_api(api_url, params)
        if city_data:
            return city_data[0]['name']
        else:
            return 'No nearest city.'

    def get_person_data(self) -> dict:
        return {
            "name": self._name,
            "email": self._email,
            "city": self._city
        }
