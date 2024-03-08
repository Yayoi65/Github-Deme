
def celsius_to_Kelvin(temp):
    return temp + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

#User input temperature
temp = float (input("enter the temperature in degrees celsius:"))

#User input measurement choice
units_of_measurement = input ('''What are the units of measurement?
                                select the appropriate number below
                                1.Degree Celsius
                                2.Kelvin'''  
                                       )
if units_of_measurement =='1':
    result = Celsius_to_kelvin(temp)
else:
    result = kelvin_to_celsius (temp)

print (f"Your temperature converted  is : {result}")