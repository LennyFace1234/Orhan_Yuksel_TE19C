import pandas as pd     # Importerar panas, numpy och matplotlib
import numpy as np
import matplotlib.pyplot as plt


genderData = pd.read_csv("Gender_Data.csv")  #läser in "Gender data" filen med hjälp av pandas i variabeln "genderData". gör samma sak med de två filerna under fast till sina egna variabler med egna namn

nationalICUData = pd.read_csv("National_Daily_ICU_Admissions.csv")

nationalDeathData = pd.read_csv("National_Daily_Deaths.csv")

framesNational = [nationalICUData, nationalDeathData] # Merge:ar, alltså sätter ihop/kombinerar innehållet av variablerna nationalICUData och nationalDeathData i en frame och sedan skapar variabeln "nationalData" för de där under

nationalData = pd.concat(framesNational)


print(nationalDeathData) # skriver ut innehållet av nationalDeathData variabeln

print(nationalICUData) # skriver ut innehållet av nationalICUData variabeln

print(genderData.head(2)) # printar, alltså skriver ut, innehållet av genderData variabeln


color = ["Blue", "Red"]  # Skapar variabel "color" och ger den färgerna "Blue" och "Red" som jag sedan tänker använda i mina grafer

genderData.plot(x ='Gender', y='Total_Cases', kind = 'bar', color = color)  # plottar en bar chart där x axeln visar kön och y axeln visar antalet covid cases. Jag titlar grafen "Total Covid Cases Each Gender" och ger den färgerna i "color" variabeln
plt.title("Total Covid Cases Each Gender")

genderData.plot.pie(y='Total_ICU_Admissions', labels = genderData["Gender"], figsize=(5, 5),autopct='%1.1f%%', startangle=90, colors = color)  #gör liknande här fast med en pie chart istället. Jag ger den värdet "ICU Admissions" från min variabel så att den visar upp de två värdena i diagrammet. Sedan ger jag de labels "gender" så att Male och Female kommer in från variabeln. Jag ger den även färgen från variabeln "color" och titeln "ICU Admissions Share Male, Female"
plt.title("ICU Admissions Share Male, Female")

nationalData.plot.line(subplots=True, color = color)  # här tar jag den kombinerade variablen "nationalData" och skriver ut den i ett linjediagram. Jag sätter även på subplots så att den visar de två datasetten i två grafer. Till sist ger jag den "color" och titlar den "Daily Deaths And ICU Admissions".
plt.title("Daily Deaths And ICU Admissions")

plt.show() # här skriver jag ut alla mina grafer så att de kommer upp på skärmen i en bild



