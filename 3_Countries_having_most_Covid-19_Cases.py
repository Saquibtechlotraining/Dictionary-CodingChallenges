# You have been given the following data about the number of COVID-19 cases in different countries:
#
# cases{ "USA": 3500000, "India": 2300000, "Brazil": 1800000, "Russia": 1200000, "France": 800000, "UK": 700000, "Turkey": 650000, "Italy": 600000, "Spain": 550000, "Germany": 500000 }
#
# Write a program to find the top 3 countries with the highest number of COVID-19 cases.

covid_19 = {
    "USA" : 3500000,
    "India" : 2300000,
    "Brazil" : 1800000,
    "Russia" : 1200000,
    "France" : 800000,
    "UK" : 700000,
    "Turkey" : 650000,
    "Italy" : 600000,
    "Spain" : 550000,
    "Germany" : 500000
}
print(covid_19)
list = []
for key, val in covid_19.items():    # Unpack of covid_19.items()
    list.append(val)
max_three = sorted(list)[-3:]        # [1800000, 2300000, 3500000]

for key, value in covid_19.items():  # Unpack of covid_19.items()
    for val in max_three:
        if val == value:
            print(f"{key}: {value}")
