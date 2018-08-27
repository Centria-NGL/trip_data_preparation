import csv
from pathlib import Path
from trip_data_extract import availableFiles



weather_current_date = str()
weather_current_hour = str()

PATH_IN = Path('./processed')
PATH_OUT = Path('./combined')

NEW_HEADER = ['ROWID','TRIPDURATION','STARTDATE','STARTTIME','STARTHOUR',
    'STARTSTATIONID','ENDSTATIONID','BIKEID','USERTYPE','BIRTHYEAR',
    'GENDER', 'COMB_WITH_WEATHER' ]

def readWeatherData():
    dict_weather_time_id = dict()
    with open('NYC_WEATHER_01.01.2013-01.03.2018.csv', 'r') as weather_file:
        weather_reader = csv.reader(weather_file, delimiter = ',')
        #skipping header
        next(weather_reader)
        for row in weather_reader:
            weather_date, weather_hour = row[1], int(row[2].split(':')[0])
            dict_weather_time_id[' '.join([weather_date, str(weather_hour)])] = row[0]
        return dict_weather_time_id

def readTripData(td_file):
    with open(td_file, 'r') as trip_data_file:
        trip_data_reader = csv.reader(trip_data_file, delimiter = ';')
        #skipping header
        next(trip_data_reader)
        for row in trip_data_reader:
            yield row

def genNewTripData():
    dict_weather_time_id = readWeatherData()

    for td_file in availableFiles(PATH_IN):
        trip_reader = readTripData(td_file)
        trip_row = next(trip_reader)
        with open(Path(PATH_OUT/td_file.name), 'w', newline='') as trip_data_file_new:
            trip_writer = csv.writer(trip_data_file_new, delimiter = ';')
            trip_writer.writerow(NEW_HEADER)
            for trip_row in trip_reader:
                trip_date = trip_row[2]
                trip_hour = int(trip_row[3].split(':')[0])
                try:
                    cmbn_weather_id = dict_weather_time_id[' '.join([trip_date, str(trip_hour)])]
                    # append weather id to trip row
                    trip_row.append(cmbn_weather_id)
                    trip_writer.writerow(trip_row)
                except KeyError:
                    trip_row.append('NULL')
                    trip_writer.writerow(trip_row)




def main():
    genNewTripData()


if __name__ == '__main__' : main()
