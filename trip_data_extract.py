import csv, logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='tripdata_etl.log',
                    filemode='w')

# indexes used to extract the fields needed.
index_wanted = (0,1,3,7,11,12,13,14)

#header of output
header_out = ['TRIPDURATION','STARTDATE','STARTSTATIONID', 'ENDSTATIONID',
                'BIKEID','USERTYPE','BIRTHYEAR','GENDER']

path_to = Path(r'./extracted/')

# Return a list of all the available trip data files
#   parameters  : path to directory
#   return      : dictionary - keys: file names, values: last modified time
def availableFiles(directory):
    path = Path(directory)
    files = [i for i in path.glob('*.csv')]
    return files

# Generate data row by row
#   paramters   :   input file
#   output      :   a list carrying a row of data
def genRow(input_file):
    with open(input_file, 'r') as input:
        reader = csv.reader(input, delimiter = ',')
        next(reader)    # skipping header
        for row in reader:
            if row:
                yield [row[i] for i in index_wanted]

# Write data to appropriate files
def writeTo(file):
    p = Path(path_to / file).with_suffix('.csv')
    with open(p, 'w', newline = '') as output:
        writer = csv.writer(output, delimiter = ';')
        writer.writerow(header_out)
        # reading and writing
        for row in genRow(file):
            writer.writerow(row)


def test():
    for f in availableFiles('.'):
        writeTo(f)

if __name__ == "__main__": test()
