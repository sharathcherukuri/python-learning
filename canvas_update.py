#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import requests, json
from pprint import pprint
import csv
import os
import xml.etree.ElementTree as ET
import timeit

from itertools import zip_longest
import xml.etree.ElementTree as ET



# API reference https://canvas.instructure.com/doc/api/submissions.html

BASE_URL = "https://unt.instructure.com/api/v1%s"
access_token = '9082~hHjXT9gx76rJyk0fHMVtHsz46YE92E4sEGcvwvfYNrL373MYI1KxdopglCzmFrYm'
course_id = '30123'  # not the sis_id but the canvas internal id
REQUEST_HEADERS = {'Authorization':'Bearer %s' % access_token}

# First, get the list of students in the course

students_endpoint = BASE_URL % '/courses/%s/students' % (course_id)
# Create a request, adding the REQUEST_HEADERS to it for authentication
not_done = True
students = []
url = students_endpoint
while not_done:
  student_request = requests.get(url,headers=REQUEST_HEADERS)
  students+=student_request.json()
  print(len(students))
  if 'next' in student_request.links.keys():
    url = student.request.links['next']['href']
  else:
    not_done = False

print ('done gettign students',len(students),'students')

# Load the response as JSON
response_data = student_request.json()
# Exit if there were no students in the returned data
if not response_data:
  print ('Sorry, there were no students registered in the course.')
  exit(0)

# Loop through the students, populating the student_ids list with their canvas ids
student_ids = [s['id'] for s in response_data]

# Build the endpoint for requesting submissions

sis_id=[]
score=[]
for studentId in student_ids:

    exurl= 'https://unt.instructure.com/api/v1/courses/''30123''/students/submissions?student_ids[]='+str(studentId)+'&grouped=1&include[]=total_scores'
    # Build the GET request parameters that are needed to fetch the submissions along with the
    # total scores (grades)
    

    req = requests.get(exurl ,headers=REQUEST_HEADERS)
  
    # Load the response as JSON
    grades = req.json()
    

    for i,val in enumerate(grades):
            #print(i,val)
            #Set up a list for enrollment data
            #Set up variables
            try:  
              student = grades[i]['sis_user_id']
              score_f = (grades[i]['computed_final_score'])
              if score_f < 60.0:
                continue
              else:
                sis_id.append(student)
                score.append(score_f)
            except KeyError:
              continue
                     
d = [sis_id, score]
export_data = zip_longest(*d, fillvalue = '')
with open('final_grades.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Sis_User_ID", "Final_score"))
      wr.writerows(export_data)
myfile.close()

                


# In[ ]:


