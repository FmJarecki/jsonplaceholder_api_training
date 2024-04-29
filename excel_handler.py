from openpyxl import Workbook
from person_data_fetcher import Person


class PersonsExcelHandler:
    @staticmethod
    def save_to_excel(persons: list[Person], name: str):
        workbook = Workbook()
        sheet = workbook.active
        sheet["A1"] = "Name"
        sheet["B1"] = "Email"
        sheet["C1"] = "City"

        for idx, person in enumerate(persons, start=2):
            person_data = person.get_person_data()
            sheet[f"A{idx}"] = person_data['name']
            sheet[f"B{idx}"] = person_data['email']
            sheet[f"C{idx}"] = person_data['city']

        workbook.save(filename=f'{name}.xlsx')
