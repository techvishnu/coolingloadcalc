def calculate_cooling_load():
    # Taking user inputs
    area = float(input("Enter the area of the building (in square meters): "))
    occupants = int(input("Enter the number of occupants in the building: "))
    building_type = input("Enter the type of building (residential, commercial, etc.): ")
    outdoor_temp = float(input("Enter the outdoor temperature (in Celsius): "))
    indoor_temp = float(input("Enter the indoor desired temperature (in Celsius): "))
    
    # Calculate cooling load based on building type
    if building_type == "residential":
        cooling_load = 100 * occupants
    elif building_type == "commercial":
        cooling_load = 150 * occupants
    else:
        print("Invalid building type")
        return
    
    # Calculate heat transfer due to conduction
    u = 30  # Overall heat transfer coefficient in W/m²°C
    q_conduction = u * area * (outdoor_temp - indoor_temp)
    
    # Calculate sensible cooling load
    sensible_cooling_load = q_conduction + cooling_load
    
    # Display the final sensible cooling load to the user
    print("Sensible Cooling Load:", sensible_cooling_load, "W")

# Call the function to calculate and display the cooling load
calculate_cooling_load()
