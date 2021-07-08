# DATA = [
#     {
#         'name': 'Facundo',
#         'age': 72,
#         'organization': 'Platzi',
#         'position': 'Technical Coach',
#         'language': 'python',
#     },
#     {
#         'name': 'Luisana',
#         'age': 33,
#         'organization': 'Globant',
#         'position': 'UX Designer',
#         'language': 'javascript',
#     },
#     {
#         'name': 'Héctor',
#         'age': 19,
#         'organization': 'Platzi',
#         'position': 'Associate',
#         'language': 'ruby',
#     },
#     {
#         'name': 'Gabriel',
#         'age': 20,
#         'organization': 'Platzi',
#         'position': 'Associate',
#         'language': 'javascript',
#     },
#     {
#         'name': 'Isabella',
#         'age': 30,
#         'organization': 'Platzi',
#         'position': 'QA Manager',
#         'language': 'java',
#     },
#     {
#         'name': 'Karo',
#         'age': 23,
#         'organization': 'Everis',
#         'position': 'Backend Developer',
#         'language': 'python',
#     },
#     {
#         'name': 'Ariel',
#         'age': 32,
#         'organization': 'Rappi',
#         'position': 'Support',
#         'language': '',
#     },
#     {
#         'name': 'Juan',
#         'age': 17,
#         'organization': '',
#         'position': 'Student',
#         'language': 'go',
#     },
#     {
#         'name': 'Pablo',
#         'age': 32,
#         'organization': 'Master',
#         'position': 'Human Resources Manager',
#         'language': 'python',
#     },
#     {
#         'name': 'Lorena',
#         'age': 56,
#         'organization': 'Python Organization',
#         'position': 'Language Maker',
#         'language': 'python',
#     },
# ]

# def run():

#     # Comprehensions solutions
#     all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
#     all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    

#     for worker in all_python_devs:
#         print(worker)


# if __name__ =='__main__':
#     run()
def read():
    numbers = []
    with open("./archives/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["sergio", "laura", "pepe", "chistian"]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
#    read()
    write()

if __name__ == "__main__":
    run()