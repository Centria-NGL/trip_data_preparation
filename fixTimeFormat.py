import csv
from pathlib import Path

PATH_IN = Path('./combined/cleaned')
PATH_OUT = Path('./combined/timeFormatFixed')

def test():
    for f in PATH_IN.glob('*TD.csv'):
        with open(PATH_OUT/f.name, 'w') as output:
            writer = csv.writer(output, delimiter = ';')
            with open(f, 'r') as input:
                print(f.name)
                reader = csv.reader(input, delimiter= ';')
                header = next(reader)
                writer.writerow(header)
                for row in reader:
                    newRow = row
                    newRow[3] = "{}".format(row[3].zfill(8))
                    newRow[4] = "{}".format(row[4].zfill(8))
                    writer.writerow(newRow)


if __name__ == "__main__" : test()
