import pyvisa
import time
import matplotlib.pyplot as plt


# Initialize the keithley and create some useful variables
multimeter = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR')# Connect to the keithley and set it to a variable named multimeter.
multimeter.write(":ROUTe:CLOSe (@101)") # Set the keithley to measure channel 1 of card 1
multimeter.write(":SENSe:FUNCtion 'TEMPerature'") # Set the keithley to measure temperature.
timeList = [] # Create an empty list to store time values in.
temperatureList = [] # Create an empty list to store temperature values in.
startTime = time.time() # Create a variable that holds the starting timestamp.

# Setup the plot 
plt.figure(figsize=(10,10)) # Initialize a matplotlib figure
plt.xlabel('Elapsed Time (s)', fontsize=24) # Create a label for the x axis and set the font size to 24pt
plt.xticks(fontsize=18) # Set the font size of the x tick numbers to 18pt
plt.ylabel('Temperature ($^\circ$C)', fontsize=24) # Create a label for the y axis and set the font size to 24pt
plt.yticks(fontsize=18) # Set the font size of the y tick numbers to 18pt


# Create a while loop that continuously measures and plots data from the keithley forever.
while True:
    temperatureReading = float(multimeter.query(':SENSe:DATA:FRESh?').split(',')[0][:-2]) # Read and process data from the keithley.
    temperatureList.append(temperatureReading) # Append processed data to the temperature list
    timeList.append(float(time.time() - startTime)) # Append time values to the time list
    time.sleep(0.5) # Interval to wait between collecting data points.
    plt.plot(timeList, temperatureList, color='blue', linewidth=10) # Plot the collected data with time on the x axis and temperature on the y axis.
    plt.pause(0.01) # This command is required for live plotting. This allows the code to keep running while the plot is shown.
