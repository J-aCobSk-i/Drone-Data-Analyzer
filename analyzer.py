def battery_consumption(flight_array):

    initial_battery = flight_array['Poziom baterii [%]'].iloc[0]  # Taking first value from column "Battery"
    if initial_battery == 'Warning - Invalid Number':
            return 'Invalid initial battery level'
    battery_left = flight_array['Poziom baterii [%]'].iloc[-1]  # Taking last value from column "Battery"
    if battery_left == 'Warning - Invalid Number':
        return 'Invalid final battery level'

    return initial_battery - battery_left

def low_battery(flight_dataframe):
    return (flight_dataframe["Poziom baterii [%]"] < 20).sum()

def maximum_altitude_time(flight_dataframe):
    index = flight_dataframe["Wysokość [m]"].idxmax()
    return flight_dataframe.loc[index, "Czas lotu [s]"]



