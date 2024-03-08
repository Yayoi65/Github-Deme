#function to convert temparatures
def celsius_to_Kelvin(temp):
    return temp + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

#User input temperature
temp = float (input("enter the temperature in degrees celsius or kelvin:"))

#User input measurement choice
units_of_measurement = input ('''What are the units of measurement?
                                select the appropriate number below
                                1.Degree Celsius
                                2.Kelvin'''  
                                       )
#change the conversion based on user input
if units_of_measurement =='1':
    result = Celsius_to_kelvin(temp)
else:
    result = kelvin_to_celsius (temp)


print (f"Your temperature converted  is : {result}")