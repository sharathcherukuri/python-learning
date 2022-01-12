import requests, json
from pprint import pprint
from urllib.request import Request, urlopen
import csv
import os
import timeit

def getInput(file):
    '''Opens the file, produces list of lines in the file, removes the header row, and returns the list'''
    inFile = open(file)
    inputList = inFile.read().splitlines()
    #print(inputList[0])
    del inputList[0]
    inFile.close()
    return inputList

def clean_data():
    '''Produces final list for use in rest of program.'''
    outlist = []
    for line in stu_lines:
          # put the line parts into a list
          items = line.split(',')
           
          #assign variables to each item to be used
          final_score = items[27]
          #print(final_score)
          SIS_user_ID = items[3]
          outlist.append([SIS_user_ID,final_score])
          #print(outlist)

    return(outlist)

#################################################################################
#   Main   Program                                                              #
#################################################################################

#Get data from input CSV file
#       CSV file in this example is in the following format:
#       Canvas SIS ID, internal Student ID, Grade Level, LastName, FirstName
stu_lines = getInput('D:\P_learning\gradebook.csv')
stu_list = clean_data()

#Enter Canvas APi token to set up API Call
token = '9082~ZtGQuTHRCfGvhjkuBXRxHTSPubyXmVjSFln9vjGI21kzGA4QOHq6o108XNvpZ0fp'
request_headers={'Authorization': token}

#Setup outfile and header
outFile = open('D:\\P_learning\\final_grades.csv', 'w')
header = ['SIS_user_ID','final_score']
columnHead = ','.join(header)
outFile.write(columnHead + '\n')

#Iterate through sudent list and set data to make API call to Canvas
count = 0
for i in stu_list:
    #set data for call to canvas and for export
    #print(i)
    user = i[0]
    #print(user)
    final_score = i[1]
    
    #prepare url using info in user and name variables
    #   This url pulls all ACTIVE courses and associated scores
    url = 'https://unt.instructure.com/api/v1/users/sis_user_id:'+user+'/courses.json?include[]=computed_final_grade&enrollment_state=active'
    
    #info for each api call
    q = Request(url)
    q.add_header('Authorization', 'Bearer ' + token)
    u = urlopen(q)

    #make the call and retrieve data
    data = json.loads(u.read().decode())
    #print(data)

    #set variables for final csv file
    part1 = [user,final_score]
    temp1 =','.join(part1)

    #iterate through JSON data to:
    #   1) edit course titles. Our course titles include the term & teacher.
    #      You may not need to edit depenging on your naming convention.
    #   2) Add edited information to a list used to build final csv
    for i,val in enumerate(data):
        #print(i,val)
        #Set up a list for enrollment data
        enroll_list = []

        #Set up variables
        enrollments = data[i]['enrollments']
        course = (data[i]['course_code'])
        print(enrollments)
        print(course)

        

        #edit course titles to remove trimester marker in course title & pull teacher name
        if course.startswith('WIN'):
            #print(course)
            teacher = course[course.rindex('-')+1:]
            point = '-' + teacher
            course1 = course[5:].rstrip(point)
            temp2 = ','.join([course1,teacher])
        else: continue
        
        #Get desired score data from JSON list
        for i,val in enumerate(enrollments):
            #print('hello')
            enroll_list.append((str((enrollments[i]['computed_current_score']))))
            enroll_list.append((str((enrollments[i]['computed_current_grade']))))

        #join data in enrollment list together
        temp3 = ','.join(enroll_list)

        #join data into final list to prepare for export
        final = [temp1,temp2,temp3]
        result = ','.join(final)
        outFile.write(result + '\n')

    #Adds to count & prints
    count += 1
    print(count)

outFile.close()

#stop timer and print final time
stop = timeit.default_timer()
print((stop-start)/60)
