# import requests as req
import matplotlib.pyplot as plt
import json

# response = req.get("https://datos.comunidad.madrid/catalogo/dataset/eb0c86dc-743d-4220-a53f-da43a8cbc955/resource/d12f9a6d-aa9c-404f-82a8-9dcaaffebc28/download/uniones_hecho_parejas.json").json()
# with open("./data/parejas.json", "w", encoding="utf8") as file:
#     json.dump(response,file, ensure_ascii=False)

with open("./data/parejas.json",encoding="utf8") as file:
    cohorte = "2010"
    data = json.load(file)["data"]
    sample_a = list(filter(lambda couple: couple["inscripcion_año"]<= cohorte ,data))
    sample_b = list(filter(lambda couple: couple["inscripcion_año"]> cohorte ,data))
    sample_n_a = sum(list(map(lambda couple: int(couple["num_inscripciones"]),sample_a)))
    sample_n_b = sum(list(map(lambda couple: int(couple["num_inscripciones"]),sample_b)))

    def divide(given_list):
        a = sum(list(map(lambda couple: int(couple["num_inscripciones"]) if couple["pareja_tipo"] == "heterosexual" else 0, given_list)))
        b = sum(list(map(lambda couple: int(couple["num_inscripciones"]) if couple["pareja_tipo"] == "homosexual femenina" else 0, given_list)))
        c = sum(list(map(lambda couple: int(couple["num_inscripciones"]) if couple["pareja_tipo"] == "homosexual masculina" else 0, given_list)))
        return a,b,c
    def by_year(given_list):
        years = sorted(set(map(lambda couple: couple["inscripcion_año"],given_list)))
        straight_list = []
        male_list = []
        female_list = []
        for year in years:
            straight = sum(list(map(lambda couple: int(couple["num_inscripciones"]) if couple["inscripcion_año"] == year and couple["pareja_tipo"] == "heterosexual" else 0,given_list)))
            male = sum(list(map(lambda couple: int(couple["num_inscripciones"]) if couple["inscripcion_año"] == year and couple["pareja_tipo"] == "homosexual masculina" else 0,given_list)))
            female = sum(list(map(lambda couple: int(couple["num_inscripciones"]) if couple["inscripcion_año"] == year and couple["pareja_tipo"] == "homosexual femenina" else 0,given_list)))

            straight_list.append((year, straight))
            male_list.append((year, male))
            female_list.append((year, female))
        return straight_list, male_list, female_list
    straight_list_2010, male_list_2010, female_list_2010 = by_year(sample_a)
    straight_list_all, male_list_all, female_list_all = by_year(data)
    print(male_list_all)
    values_straight_all = list(map(lambda couple: couple[1],straight_list_all))
    values_male_all = list(map(lambda couple: couple[1],male_list_all))
    values_female_all = list(map(lambda couple: couple[1],female_list_all))

    years_all = list(map(lambda couple: couple[0],straight_list_all))
    
    by_year(sample_a)
    sample_a_straight,sample_a_fem,sample_a_male = divide(sample_a)
    sample_b_straight,sample_b_fem,sample_b_male = divide(sample_b)
    # print((sample_a_fem + sample_a_male)/sample_n_a)
    # print((sample_b_fem + sample_b_male)/sample_n_b)
    # plt.plot(years_1995_2010, values_straight_2010)
    # plt.plot(years_1995_2010, values_male_2010)
    print(len(years_all), len(values_straight_all))
    plt.plot(years_all, values_straight_all, label="heterosexual")
    plt.plot(years_all, values_male_all, label="male")
    plt.plot(years_all, values_female_all, label="male")

    
    plt.legend()
    plt.show()

