# tech_challenge_octopus

Pre-requisities:
   * Python 3 installed
   * Django installed
   * A web-browser or curl installed
   
Please follow these steps to make readings from csv files

1. Unzip the tar package and go inside the directory
2. go inside the project folder coding_challenge
3. Upload the .csv files into the /csv directory 
4. From project folder, run following commands
            - python3 manage.py makemigrations  (in case migrations have not been applied)
            - python3 manage.py migrate
            - python3 manage.py runserver (to start the server)
            
5. Create super user for admin panel using following command
            - python3 manage.py createsuperuser
            - Then provide username, email-address and password to the console 
            
6. Go to "127.0.01:8000/meter_readings/" from web-browser or using curl command - "curl 127.0.01:8000/meter_readings/"
           
           Response Code   Response Message                          Intepretation
           201             Data successfuly uploaded                 .csv files are read and models are created successfully
           
           400             {                                         some .csv files are wrong formatted and/or duplicated. Other files                                                                      successfully uploaded
                              wrong_format_files : [file-names],
                              duplicate_files: [file_names]
                           }
           404             files not found                          No files found in /csv folder
           
 7. View meter readings in admin panel
          - Go to admin panel by "127.0.01:8000/admin/
          - Login using super user username and password
          - To view Meter go to /meter_reading/reading/
          - search by NMI or meter serial number if required

Run Tests

* From project directory, apply following command to run tests
          - python3 manage.py test
          
* Available Test Cases
         1.  test_write_data_to_model - Verify correct formatted data are stored in the database
         2.  test_write_wrong_formatted_data - Verify wrong formatted data are not inserted and it throws ValueError
         
     Possible Test Cases:
        Due to the time constraint, I was unable to write test cases for following scenarios. But manual testing was 
        conducted
         * Verify the system captures all the available files within the given directory
         * Verify the correct http response is given for each possible scenario
         * Verify that data are not inserted to the database from two csv files with the same name         
         
         
 Assumptions
 
 - According to the NEM13 data guide, the csv file is created with a unique name.
 - Since the data files does not have column names, the format of data does not change in all files
 - Header data and terminal data does not required to inserted to the database
 
 Improvements
 
 - Admin site can be further improved to accommodate users with restricted privileges
 
 