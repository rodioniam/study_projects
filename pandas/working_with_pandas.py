import pandas as pd


a = pd.DataFrame([[1, 5, 6, 3], [1, 5, 6, 3]], index=['station_1', 'station_2'],
                 columns=['wind', 'solar', 'pressure', 'speed'])
print(a)


# wind, solar, pressue, speed - labels
# station_1, station_2 - indexes
# series is just one column from dataframe
