# Importing All the Python Inbuit Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV file and Print it
df_data = pd.read_csv("U.S. Military Deaths by cause 1980-2010.csv")
print(df_data)

# Deleting the pending column from dataframe using drop function
df_data.drop('Pending ',inplace=True, axis=1)  #Non Use Column
print(df_data) # Print the Dataframe

# Creating the  Line plot of the Total Military FTE along with seperate category of Service
plt.figure(dpi=300) #To Create figure
plt.plot(df_data["Calendar Year"], df_data["Active Duty"], label="Active Duty") # Plot the Line Grapgh
plt.plot(df_data["Calendar Year"], df_data["Full-Time (est) Guard+Reserve"], label="Full-Time (est) Guard+Reserve") # Plot the Line Grapgh
plt.plot(df_data["Calendar Year"], df_data["Selected Reserve FTE"], label="Selected Reserve FTE") # Plot the Line Grapgh
plt.plot(df_data["Calendar Year"], df_data["Total Military FTE"], label="Total Military FTE") # Plot the Line Grapgh

# Setting X,Y labels,showing the legends and Title
plt.xlabel("Calendar Year") # Setting the X lable of the graph
plt.ylabel("Number of military personnel(USA)") # Setting the Y lable of the gragh
plt.xlim(1980,2010) # Limit the grapgh range within the limit
plt.title("USA MILITARY FTE ") # Providing the Title to the graph
plt.grid(True) #To show grid in Plot 
plt.legend() #To show the elements of the graph

# Save the plot Image in JPEG formate
plt.savefig("Total Military FTE.jpeg",dpi=300)
plt.show() #To show the plot

# Ploting the subplots for total death with causes of death
plt.figure(figsize=(10,10)) 
plt.suptitle("Total Death of Military Person and Cause of Death(1980-2010,USA)", fontsize=15) #To generate the subplot title

plt.subplot(2,2,1) #To create first plot of subplot
plt.plot(df_data["Calendar Year"], df_data["Total Deaths"],color='red', label="Total Death")
plt.xlabel("Calendar Year")
plt.ylabel("Number of military personnel(USA)")
plt.xlim(1980,2010)
plt.grid(True)
plt.title("Plot-1") #To provide the title to first plot
plt.legend()

plt.subplot(2,2,2) #To create second plot of subplot.
plt.plot(df_data["Calendar Year"], df_data["Accident "],color='green', label="Accident")
plt.plot(df_data["Calendar Year"], df_data["Hostile Action"],color='purple', label="Hostile Action")
plt.xlabel("Calendar Year")  
plt.ylabel("Number of military personnel(USA)")
plt.xlim(1980,2010)
plt.grid(True)
plt.title("Plot-2") #To provide the title to second plot
plt.legend()

plt.subplot(2,2,3) #To create third plot of subplot
plt.plot(df_data["Calendar Year"], df_data["Homicide "],color='orange', label="Homicide")
plt.plot(df_data["Calendar Year"], df_data["Illness "],color='blue', label="Illness")
plt.xlabel("Calendar Year")
plt.ylabel("Number of military personnel(USA)")
plt.xlim(1980,2010)
plt.grid(True)
plt.title("Plot-3") #To provide the title to Third plot
plt.legend()

plt.subplot(2,2,4) #To create forth plot of subplot
plt.plot(df_data["Calendar Year"], df_data["Self-Inflicted"],color='black', label="Self-Inflicted")
plt.plot(df_data["Calendar Year"], df_data["Terrorist Attack"],color='red', label="Terrorist Attack")
plt.plot(df_data["Calendar Year"], df_data["Undetermined "],color='green', label="Undetermined ")
plt.xlabel("Calendar Year")
plt.ylabel("Number of military personnel(USA)")
plt.xlim(1980,2010)
plt.grid(True)
plt.title("Plot-4") #To provide the title to forth plot
plt.legend(loc="center right")
plt.savefig("Sub_plot.jpeg",dpi=300) #Save the plot Image in JPEG formate
plt.show() #To show the plot


# Sum of All Column and Print
Sum_of_Col = df_data.sum(axis=0)
print(Sum_of_Col)

# Making a new data Frame and Print
column_Name = {'Cause of Death':['Accident','Hostile','Homicide','Illness','Self-Inflicted','Terrorist Attack','Undetermined'],'Count of Death':[25073,4814,2329,8579,6911,420,629]}
New_data = pd.DataFrame(column_Name) # Assign variable name
print(New_data)

# Ploting the Pie chart for making comparison of cause of death
plt.figure(figsize=(5,5))
plt.pie(New_data['Count of Death'],labels=New_data['Cause of Death'],explode= (0,0.1,0.1,0.1,0.1,0.1,0.1),rotatelabels=True,autopct='%1.0f%%',shadow=False,labeldistance=1.01,radius=0.7,pctdistance=0.8)
plt.title("Comparision Of Various Causes of Death",loc="center",fontsize=10)
plt.savefig("Pie_chart.jpeg",dpi=300)
plt.show() #To show the plot

# Ploting the Bar Chart 
plt.figure(figsize=(5,5))
df_data.plot.bar(x ='Calendar Year', y = ['Total Deaths','Accident ', 'Illness ', 'Self-Inflicted'], rot = 'vertical', width = 0.7) # Ploting the Bar Chart
plt.xlabel("Calendar Year")
plt.ylabel("Number of military personnel(USA)")
plt.title("Total Death Vs Cause of Death(1980-2010,USA)",loc="center",fontsize=10) 
plt.savefig("Total Death Vs Cause of Death.jpeg",dpi=600) # Save the plot Image in JPEG formate
plt.legend()
plt.show() #To show the plot



