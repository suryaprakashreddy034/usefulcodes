from csv import writer
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


row_contents = [32,'Shaun','Java','Tokyo','Morning']
# Append a list as new line to an old csv file
append_list_as_row('/home/surya/Desktop/facerec_codes/attendence/tmp.csv', row_contents)

import datetime;
  
# ct stores current time
ct = datetime.datetime.now()
print("current time:-", str(ct))
  
# ts store timestamp of current time
ts = ct.timestamp()
print("timestamp:-", ts)