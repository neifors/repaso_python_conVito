# import requests as req
# import threading
# import concurrent.futures
# import time
# user = input("What country 1?: ")

# Thread 1
# def get_data(input):
#     return req.get(f"https://restcountries.eu/rest/v2/name/{input}").json()
# while user != "q":
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         future1= executor.submit(get_data, user)
#         user2 = input("What country 2?: ")
#         return_value1 = future1.result()
#         print(return_value1)
#         future2= executor.submit(get_data, user2)
#         return_value2 = future2.result()
#         print(return_value2)
#         user = "q"

# Thread 2
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     start = time.perf_counter()
#     def get_data():
#         return req.get(f"https://restcountries.eu/rest/v2/name/argentina").json()
#     f1 = executor.submit(get_data)
#     print(f1.result())
#     f2 = executor.submit(get_data)
#     print(f2.result())
#     f3 = executor.submit(get_data)
#     print(f3.result())
#     f4 = executor.submit(get_data)
#     print(f4.result())
#     f5 = executor.submit(get_data)
#     print(f5.result())
#     finish = time.perf_counter()
#     print(round(finish-start, 2))
# NO THREAD 2
# start = time.perf_counter()
# def get_data():
#     return req.get(f"https://restcountries.eu/rest/v2/name/argentina").json()
# f1 = get_data()
# print(f1)
# f2= get_data()
# print(f2)
# f3 = get_data()
# print(f3)
# f4 = get_data()
# print(f4)
# f5 = get_data()
# print(f5)
# finish = time.perf_counter()
# print(round(finish-start, 2))

# user_no1 = input("What country 1?: ")
# result1 = req.get(f"https://restcountries.eu/rest/v2/name/{user_no1}").json()
# user_no2 = input("What country 2?: ")
# print(result1)
# result2 = req.get(f"https://restcountries.eu/rest/v2/name/{user_no2}").json()
# print(result2)


import requests as req
import csv
import json
import concurrent.futures

text = "By country or by region?: "
user = input(text)
results = []
while user != "q":
    def get_country(country):
        return req.get(f"https://restcountries.eu/rest/v2/name/{country}").json()
    if user == "country":
        user = input("Which country?: ")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(get_country, user)
            print("Just a sec...")
            response = future.result()
            print(response)
            with open("countries.csv", "a") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(response)
            print(response[0]["name"],response[0]["population"], response[0]["languages"][0]["name"])
            user = input(text)
    elif user == "region":
        user = input("Africa\nAmericas\nAsia\nEurope\nOceana\nFrom the list, which region? ")
        response = req.get(f"https://restcountries.eu/rest/v2/region/{user}").json()
        with open(f"{user}.json", "w") as file:
            json.dump([element for element in response], file)
        print("Contries have been added")
        user = input(text)
    else:
        print("Sorry, we don't have that option available yet")
        user = input(text)