from person_data_fetcher import Person, get_data_from_api
from json_handler import PersonsJSONHandler
from excel_handler import PersonsExcelHandler

if __name__ == '__main__':
    persons_api_url = 'https://jsonplaceholder.typicode.com/users'
    persons: list[Person] = []
    for data in get_data_from_api(persons_api_url):
        person = Person(data)
        persons.append(person)
        print(person)

    PersonsExcelHandler.save_to_excel(persons, 'excel_test')

    PersonsJSONHandler.save_to_json(persons, 'persons')
    PersonsJSONHandler.read_from_json('persons')
