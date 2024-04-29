import json
from person_data_fetcher import Person


class PersonsJSONHandler:
    @staticmethod
    def save_to_json(persons: list[Person], name: str):
        serialized = []
        for person in persons:
            serialized.append(person.get_person_data())

        with open(f'{name}.json', 'w') as json_file:
            json.dump(serialized, json_file)

    @staticmethod
    def read_from_json(name: str):
        with open(f'{name}.json', "r") as json_file:
            persons_data = json.load(json_file)

        print(persons_data)
