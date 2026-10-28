# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 13:35:28 2026

@author: bella
"""

from Course import Course

#===========================================
"""
Begin by creating Course objects and adding them to a list structure
"""

course_1 = Course('IS3073',
                  'Spring 2026',
                  'B+')

course_2 = Course('IS3003',
                  'Spring 2026',
                  'A+')

course_3 = Course('ACC1003',
                  'Spring 2026',
                  'C')

course_list = [course_1, course_2, course_3]

#===========================================
# List each object in the course list

def list_courses (course_list: list) -> None:

    print ("      Course     Semester     Grade")
    
    line_number = 0
    
    for course in course_list:
        line_number += 1
        print(line_number, course)
    # end iteration
        
#end function


#==========================================


def calculate_GPA (transcript:list) -> float:
    
    #Instantiate and Initialize accummulators
    total_hours = 0 
    total_points = 0.0
    
    #Create a dictionary for translating grade into points
    quality_points = { 'A+' : 4.00, 'A' : 4.0, 'A-': 3.67,
                       'B+' : 3.33, 'B' : 3.0, 'B-': 2.67,
                       'C+' : 2.33, 'C' : 2.0, 'C-': 1.67,
                       'D+' : 1.33, 'D' : 1.0, 'D-': 0.67,
                        'F' : 0.00  }

    #Iterate through list, calculating values for each Course oject
    for course in transcript:
        #Deriving the course hours
        """
        Turning the hours into an integer, and getting the last digit of
        the course code
        """
        hours = int(course.get_crs_code()[ -1 ])
        
        #Calculate Quality Points
        pts = quality_points[ course.get_crs_grade()] * hours
        
        #Accummulate
        
        total_hours += hours
        total_points += pts
        #End iteration
        
    return total_points / total_hours
# End function
    


def add_course(transcript:list) -> None:
    from validations import (validate_code, 
                             validate_semester, 
                             validate_grade)
    
    #Start by setting a loop control variable
    valid = False
    
    while valid == False:
        code = input("\nPlease enter a valid course code: ")
        valid = bool(validate_code(code))
        
        if valid == False:
            print("The format is 2-4 CAPITAL letters followed by 4 digits.")
        #end selection
    #end iteration
    
    #Start by setting a loop control variable
    valid = False
    
    while valid == False:
        semester = input("\nPlease enter a valid semester: ")
        valid = bool(validate_semester(semester))
        
        if valid == False:
            print("Please enter a valid semester as 'Season' followed " +
                  "by a space, followed by a four digit year.")
        #end selection
    #end iteration
    
    #Start by setting a loop control variable
    valid = False
    
    while valid == False:
        grade = input("\nPlease enter a valid grade: ")
        valid = bool(validate_grade(grade))
        
        if valid == False:
            print("Letter grades are A-F with a (+) or a (-) as appropiate.")
        #end selection
    #end iteration
    
    new_course = Course(code,
                        semester,
                        grade)
    
    transcript.append(new_course)
    
# end function


def update_course( transcript : list ) -> None:
    """
    Import validation functions for semester & grade
    """
    from validations import validate_semester, validate_grade
    
    # We will present the user with a List of Course objects
    list_courses(transcript)
    
    # Prompt for which course object to update
    index = int(input("By number, which course do you want to update?: "))
    
    if (index <= len(transcript)) and ( index > 0):
        
        index -= 1
        target = transcript[index]
        
        update_OK = True
        
        new_semester = input("Enter the correct semester: ")
        if validate_semester(new_semester) == False:
            update_OK = False
        # end selection
        
        new_grade = input("Enter the correct grade: ")
        if validate_grade(new_grade) == False:
            update_OK = False
        # end selection
        
        if update_OK == True:
            # Do the update
            target.set_crs_semester(new_semester)
            target.set_crs_grade(new_grade)
            
            print("Update successful.")
            
        else:
            print("Some of your data is invalid. Update canceled.")
        
    else:
        print("I am sorry, that Course does not exist. ")
        
    # end selection
# end function


#=========================================================
list_courses(course_list)

print("GPA Calculated as: ", calculate_GPA(course_list))
    
#add_course(course_list)

list_courses(course_list)

print("\n\n\n")
update_course(course_list)

list_courses(course_list)
    
    
    
    
    
    