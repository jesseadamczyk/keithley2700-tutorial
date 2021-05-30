import pyvisa

multimeter = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR') # Connect to the keithley and set it to a variable named multimeter.

#multimeter.write(":ROUTe:CLOSe (@101)") # Set the keithley to measure channel 1 of card 1

multimeter.write(":SENSe:FUNCtion 'TEMPerature'") # Set the keithley to measure temperature

#print(multimeter.query(':SENSe:DATA:FRESh?')) # Collect the most recently measured data

multimeter.write(":ROUTe:OPEN:ALL") # Open all card channels and thereby set the keithley to measure the front panel inputs.

print(multimeter.query(':SENSe:DATA:FRESh?')) # Collect the most recently measured data