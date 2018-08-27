import csv
from pathlib import Path
from trip_data_extract import availableFiles

header_out = ['ROWID','TRIPDURATION', 'STARTDATE', 'STARTTIME',
                'STARTHOUR', 'STARTSTATIONID', 'ENDSTATIONID',
                'BIKEID', 'USERTYPE', 'BIRTHYEAR', 'GENDER']

path_in = Path(r'./prcsd/')
path_to = Path(r'./processed/')

ROWID = int()

def process(row):
    processed_row = row
    processed_row[3] = '{}:00:00'.format(row[3].split(':')[0])
    return processed_row

def genData(file):
    with open(file, 'r') as input:
        reader = csv.reader(input, delimiter = ';')
        next(reader)
        for row in reader:
            yield process(row)

def write(file):
    with open(Path(path_to / file).with_suffix('.csv'), 'w', newline = '') as output:
        writer = csv.writer(output, delimiter = ';')
        writer.writerow(header_out)
        for row in genData(Path(path_in / file)):
            ROWID += 1
            row.insert(0, '{}'.format(zfil(hex(ROWID), 20)))
            writer.writerow(row)


def test():
    ROWID = 0
    for f in availableFiles(path_in):
        with open(Path(path_to / f.name).with_suffix('.csv'), 'w', newline = '') as output:
            writer = csv.writer(output, delimiter = ';')
            writer.writerow(header_out)
            for row in genData(f):
                row.insert(0, '{}'.format(format(ROWID, 'X')).zfill(20))
                writer.writerow(row)
                ROWID += 1

if __name__ == "__main__": test()
