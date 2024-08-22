import json as js

filename1 = input("Введите путь к файлу values: ")
filename2 = input("Введите путь к файлу tests: ")
filename3 = input("Введите путь к файлу report: ")
with open(filename1, 'r') as f1:
    values = js.load(f1)["values"]
with open(filename2, 'r') as f2:
    tests_structure = js.load(f2)

def fill_report_structure(tests_structure, values):
    if isinstance(tests_structure, list) == True:
        for testitem in tests_structure:
           testid =  testitem["id"]
           for valueitem in values:
               if valueitem["id"] == testid:
                  testitem["value"] = valueitem["value"]
           for k, v in testitem.items():
               if k == "values":
                   fill_report_structure(testitem["values"], values)
        return tests_structure

fill_report_structure(tests_structure["tests"], values)
with open(filename3, "w") as reportfile:
    js.dump( tests_structure, reportfile, indent=4)