"""Read a csv and transform this in a dictionary"""
import csv

def read_csv(path):
    with open(path, 'r') as csv_read:
        reader = csv.reader(csv_read, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            it = zip(header, row)
            dictionary = {key:value for key, value in it }
            data.append(dictionary)
        return data


if __name__=='__main__':
    read_csv('./world_population.csv')