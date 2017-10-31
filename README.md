Welcome to Python Address2Elevation, one of the many places online that you can convert Addresses to Elevations.

There are two options for conversion: Bulk Entry using a .csv file or manually entering via typing in your own array.

A tkinter gui can be added to provide additional simplicity but for the sake of this project, ill keep the code within the py files.

Step 1- Choose whether you would like to do a bulk entry or a string entry.

Option 1- Bulk Entry- 

-Create a .csv file similar to the Addresses.csv in the git repository

-Within Address2Elevation.py, make sure that the following lines are commented out as shown:

#String Entry- Uncomment the below line if you plan on enterying addresses manually
#addresses = [<address 1>,<address 2>,<address 3>...<address n>]

-Ensure that the following lines are not commented out (as shown)

filename = '<LOCATION + FILENAME.csv>'
with open(filename) as csvfile:
    address_reader = csv.reader(csvfile)
    for row in address_reader:
        addresses.append(row[0])

-Change <LOCATION + FILENAME.csv> to the Addresses.csv file you created

Option 2- String Entry- 

-Within Address2Elevation.py, make sure that the following lines are commented out as shown:

String Entry- Uncomment the below line if you plan on enterying addresses manually
addresses = [<address 1>,<address 2>,<address 3>...<address n>]

-Update the addresses line by replacing <address x> with the addresses you would like to find elevations for.

-Ensure that the following lines are commented out (as shown)
#filename = '<LOCATION + FILENAME.csv>'
#with open(filename) as csvfile:
#    address_reader = csv.reader(csvfile)
 #   for row in address_reader:
 #       addresses.append(row[0])

Step 2- Update the following line as to where you would like to save a .csv file (if required) If not required, comment out

the_file_name_v2 = '<LOCATION OF FINAL READOUT>'

Step 3- Compile and run using a python IDE.


Notes-
- The Google API can run slow and python runs very fast (not a great combo). I added a bunch of time delays within the source code. If you run into issues with it giving errors, change the delays to longer times.
