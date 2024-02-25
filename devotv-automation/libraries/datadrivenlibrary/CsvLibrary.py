from csv import reader, DictWriter, DictReader, writer
import os

__author__ = 'Manish Pandey'


class CsvLibrary(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.data = []

    @staticmethod
    def read_data_from_file(filename):
        with open(filename, 'r') as content:
            data = content.read()
        return data

    @staticmethod
    def read_csv_file(filename):
        """This creates a method named "Read CSV File"

        This method takes one argument, which is a path to a .csv file. It
        returns a list of rows, with each row being a list of the data in
        each column.
        """
        data = []
        with open(filename, 'r') as csvfile:
            csvdata = reader(csvfile)
            for row in csvdata:
                data.append(row)
        csvfile.close()
        return data

    @staticmethod
    def get_num_of_active_rows_csv(filename):
        """This keyword will count the number of rows on specified file
        This is useful when doing cycles x times
        where x is the file size (rows)
        """
        with open(filename) as f:
            try:
                return sum(1 for line in f)
            finally:
                f.close()

    @staticmethod
    def read_from_csv_in_dict(filename, row_num):
        """
         reads from csv by index(row_number)
         :param filename:
         :param row_num:
         :return:
         """
        file = open(filename, 'r')
        csvdata = DictReader(file)
        for r, items in enumerate(csvdata):
            if r == (int(row_num) - 1):
                return items
        file.close()

# a = [1,2,3,4,5]
# a.append(6)
# a= 1
# print(a) ==>
# a = {1:a,2:b, 3:d} ==> a[2]=c
# capturing the content a variable from file
# manupulation on that data into variable
# your new data is ready into a variable
# save the variable content into file
# a = None

    @staticmethod
    def write_to_csv_in_dict(filename, data):
        """
         write in to csv by in next line with header ( if file not exist )
         :param path_to_csv_file: ~/testdata/csv
         :param data: {'page':'application-page','domain':'navyfederal'}
         :return:
         """
        with open(filename, 'a', newline='') as csvfile:
            fieldnames = list(data.keys())
            write = DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                write.writeheader()
            write.writerow(data)
        csvfile.close()

    @staticmethod
    def path_to_file(path_to_csv_file, filename):
        """
        :param path_to_csv_file:
        :param filename:
        :return:
        """
        return (path_to_csv_file + filename + ".csv")
