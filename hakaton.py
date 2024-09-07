workers = {
    "1":{
        "Прізвище":"Федорчук",
        "Посада":"Data Analyst",
        "KE":4,
        "Проєкти":["khgsdkh", "lahd", "skljhf"]
    },
    "2":{
        "Прізвище": "Григоренко",
        "Посада": "Geodata Techiclan",
        "KE":5,
        "Проєкти":["kjfalhi", "laidjl", ".aksjddhp"]
    },
    "3":{
        "Прізвище": "Василенко",
        "Посада": "Programer",
        "KE":9,
        "Проєкти":["s;lkhf;", "jshflij", "slfl"]
    }  
}
print("Прізвища всіх співробітників:")
for work in workers:
    print("-", workers[work]["Прізвище"])

print("Посади усіх співробітників:")
for work in workers:
    print("-", workers[work]["Посада"])
############################
Kof = 0
Fio = ""

##############################
print("Прізвище найефективнішого співробітника:")
for work in workers:
    if Kof < workers[work]["KE"]:
        Kof = workers[work]["KE"]
        Fio = workers[work]["Прізвище"]
print("-", Fio)
print("-", Kof)
