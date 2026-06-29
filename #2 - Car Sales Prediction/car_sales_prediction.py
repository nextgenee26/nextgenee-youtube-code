# Hey guys, today we will be predicting the price we sell our car at based on mileage and production year
# Lets get started!

# Thank you guys for watching, the code will all be placed in the description down below
# Don't forget to subscribe and like and share the video, it will really help me, thanks everyone!

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./cars.csv")

price_bought = []
price_sold = []
price_change = []

for i in range(len(df)):
  price_bought.append(df.iloc[i, 4].item())
  price_sold.append(df.iloc[i, 5].item())
  price_change.append(price_sold[i] - price_bought[i])

df["Price Change"] = price_change
df["Year Change"] = 2026 - df["Year"]

mileage_corr = df["Mileage"].corr(df["Price Change"])
year_corr = df["Year Change"].corr(df["Price Change"])

print(df)
print()
print("Mileage Correlation: ",mileage_corr)
print("Year Correlation: ",year_corr)  #remember the closer the correlation coefficient to -1 or 1, the stronger it is
print()

if mileage_corr > year_corr:
  print("Year correlation is much stronger")
elif mileage_corr < year_corr:
  print("Mileage correlation is much stronger")

x_mileage_values = df["Mileage"]
x_year_values = df["Year Change"]
y_values = df["Price Change"]

m_mileage, b_mileage = np.polyfit(x_mileage_values, y_values, 1)
m_year, b_year = np.polyfit(x_year_values, y_values, 1)

mileage_reg = m_mileage * x_mileage_values + b_mileage
year_reg = m_year * x_year_values + b_year

plt.subplot(2, 1, 1)
plt.scatter(x_mileage_values, y_values)
plt.plot(x_mileage_values, mileage_reg, color="green")
plt.title("Mileage vs Price Change")

plt.subplot(2, 1, 2)
plt.scatter(x_year_values, y_values)
plt.plot(x_year_values, year_reg, color="red")
plt.title("Year vs Price Change")

user_mileage = int(input("How many miles has your car driven?: "))
user_year = int(input("What year was car made in? [The year date only works from 2020 to 2025]: "))
user_bought = int(input("How much did you buy the car for?: "))

m_mileage = float(m_mileage.item())
m_year = float(m_year.item())

predicted_mileage = (user_bought + (m_mileage * user_mileage + b_mileage))
predicted_year = (user_bought + (m_year * (2026 - user_year) + b_year))
predcited_total = (predicted_year + predicted_mileage) / 2

print("Your car based on mileage is expected sell for: ", predicted_mileage)
print("Your car based on mileage is expected sell for: ", predicted_year)
print("The average between the two come at: ", predcited_total)

plt.show()
