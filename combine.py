import csv, logging, os.path

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='tripData.log',
                    filemode='w')

header = ("ROWID", "TRIPDURATION", "STARTDATE", "STARTTIME",
        "STARTSTATIONID", "ENDSTATIONID",
        "BIKEID", "USERTYPE", "BIRTHYEAR", "GENDER" )

def genDataFiles():
    import glob
    for data_file in glob.glob("*.csv"):
        yield data_file

def processed(row):
    l = row
    duration = convertSecToTime(int(l[1]))
    l[1] = duration
    return l

def convertSecToTime(tripDuration):
    s = tripDuration
    min = 0
    hour = 0
    while (s >= 60):
        s -= 60
        min += 1
    while (min >= 60):
        min -= 60
        hour += 1
    return "{}:{}:{}".format(str(hour).zfill(2), str(min).zfill(2), str(s).zfill(2))

# read csv
def genTripData(f_data):
    try:
        with open(f_data,buffering=20000000) as f:
            fileReader = csv.reader(f, delimiter = ';')
            next(fileReader)
            for line in fileReader:
                if line:
                    yield processed(line)
    except:
        logging.exception('ISSUE READING TRIP DATA')

def main():
    for f in genDataFiles():
        path = ("TRIPDATA_2013.csv")
        with open(path, 'a') as output:
            fileWriter = csv.writer(output, delimiter=';')
            fileWriter.writerow(header)
            for data in genTripData(f):
                fileWriter.writerow(data)

if __name__ == '__main__':
    main()
