# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

#checking which countrie(s) have the largest percentage 
#Armenia & Maldives (Chose Armenia)
#largePercentBooleanList = lwd["EI_women_elec_p"].between(99,100)
#largePercentData = lwd.loc[largePercentBooleanList]
#print(largePercentData["country_name"].unique())

#checking whcih countrie(s) have the smallest percentage
#Liberia
#smallPercentBooleanList = lwd["EI_women_elec_p"].between(0,2)
#smallPercentData = lwd.loc[smallPercentBooleanList]
#print(smallPercentData["country_name"].unique())

#one country data (for Armenia and Liberia)

armeniaBooleanList = lwd["country_name"] == "Armenia"
armeniaData = lwd.loc[armeniaBooleanList]
liberiaBooleanList = lwd["country_name"] == "Liberia"
liberiaData = lwd.loc[liberiaBooleanList]


# Print out the number of rows and columns
print(lwd.shape)
print("Armenia suffered a genocide from 1915 to 1916, where as many as 1.2 million Armenian Christian people died from massacres, indivisual killings, and starvation.")
print("However, Armenia was able to significantly recover from this and become one of the countries that have almost 100% women living in households with access to electricity.")

input("Press return to countinue. \n")

print("Liberia was the first African republic to proclaim indepence, making it Africa's oldest modern republic.")
print("Yet, due to a devestating civil war and disease, the economy declined, and now has almost 0% of women live in households with electricity.")

input("Press return to countinue. \n")

print("Hence, it is important to think about the research questions: How do the lives of Armenians and Liberians differ in present day? & What historical events and changes caused the present situation?")

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
plt.scatter(armeniaData["year"],armeniaData["EI_women_elec_p"],color="red")
plt.scatter(liberiaData["year"],liberiaData["EI_women_elec_p"],color="blue")

# add a title to the plot
plt.title("Women living in a household with electricity (%) over time")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women living in a household with electricity (%)")


# show the plot
plt.show()