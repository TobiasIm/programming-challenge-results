import csv
import os
import my_settings as ms

#In the following lines there are the accessing paths for the original csv-files for the tasks independent of the OS
myvarpath_weather = os.path.join(ms.main_path, 'weather.csv')
myvarpath_calculatedWeather = os.path.join(ms.out_path, 'calculated_weather.csv')


#TODO: Detailed formulation at the beginning of each method

class FileReaderWriter():
    '''A class used to load, create and calculate values from csv-file
    
    ...

    Attributes
    ----------
    infile: e.g. csv-file
        a file that is given and has to be load to work with it 
    outfile: e.g. csv-file
        creating a csv-file to safe extracted and calculated values
    minMax: str
        determines either min or max value that should be presented in the terminal
    absolute: boolean
        either True or False for the absolute value

    Methods (one example!)
    ---------
    read(fieldname1, fieldname2, fieldname3, fieldname4, delimiter, row1, row2, row3)
        fieldnames are headernames
        rows are the rownames which should be load from the original csv-file

        Loads the original csv file and iterates row by row. Then calculates the diff between two values 
        and safe it into var diff. After this step the result and the regarding values are safed into an new csv-file.
    '''

    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile


    def read(self, fieldname1, fieldname2, fieldname3, fieldname4, delimiter, row1, row2, row3):
        '''method to load the csv-file and calculate two columns with the method ___calculate___. Afterwards safe the result into new csv-file'''

        #Generate a new csv-file for the output of calculation
        outfile = open(self.outfile, "w", newline="")
        writer = csv.DictWriter(outfile, fieldnames = [fieldname1, fieldname2, fieldname3, fieldname4])#generation of the header for the new csv-file
        writer.writeheader()

        #opens the original csv file       
        with open(self.infile, "r") as file:
           reader = csv.reader(file, delimiter=delimiter)
           header = next(reader)
           
           for row in reader:
               column1 = row[row1]
               column2 = row[row2]
               column3 = row[row3]
               
               diff = self.__calculate__(column2, column3)#method for calculation of the difference between two columns
               
               #print(column1, column2, column3, diff)
               line = "{}, {}, {}, {}\n".format(column1, column2, column3, diff)#each calculation result and its refering columns are safed in new csv-file line by line
                          
               outfile.write(line)
        outfile.close()

    def __calculate__(self, column1, column2):
        '''This method calculates the difference between two given columns, either absolute or relative difference'''

        #check the datatype of values and change it if necessary
        if not isinstance(column1, float) or not isinstance(column2, float):
                   column1 = float(column1)
                   column2 = float(column2)

        #either absolute value or just the difference has to be calculated, depend on the users goal       
        diff = column1 - column2

        return diff

#Generation of the objects from class FileReader with the parameters to get the solution described in the task "programming challenge"
data_weather = FileReaderWriter(myvarpath_weather, myvarpath_calculatedWeather) #FileReader(path to original csv-file, path to manipulated csv-file, either "min" or "max" for Maximum or Minimum difference, absolute value == True)
data_weather.read("Day", "weather_maxTemp", "weather_minTemp", "weather_diff", ",", 0, 1, 2) #read(first fieldname e.g. "Day" or "Team" for new csv, second fieldname, third fieldname, calculated fieldname, delimiter, 
                                                                                            #rownumber from original for first fieldname, rownumber second, rownumber third)