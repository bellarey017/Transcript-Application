"""
This is a Transcript Application, it will allow Users to record all their 
completed Courses, add or update Course objects, and calculate their GPA.

The Transcript will be store permanently as a PICKLE file.
"""

from Course import Course

"""
Name:           add_course
Purpose:        This function will add a course using user input. The course
                will consist of the code, semester and grade. Using this information
                the function will update it to the transcript list if valid.
                If the course entered is not valid, it will re-direct the user.
Argument:       The function accepts a list called transcript (the candidates transcript).
Returns:        The function does not return a value.
"""

def add_course(transcript:list) -> None:
    
    """
    Using the validations file, the function imports the validation functions
    from that file. These functions will be utilized to ensure that the input
    value the user presents is properly formatted.    
    """
    from validations import (validate_code, 
                             validate_semester, 
                             validate_grade)
    
    #Start by setting a loop control variable
    valid = False
    
    """
    Three while loops will be set up using the control variable. It will allow the
    user to enter a value, then call the appropiate validation function to make
    sure the value follows the requirements. This will occur for the courses code,
    semester, and grade. If the input does not follow the format, then it will
    re-direct the user.
    """
    
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
    
    # Creating a new course using the values inputted
    new_course = Course(code,
                        semester,
                        grade)
    
    # Appending the new course to the candidate's transcript.
    transcript.append(new_course)  
    
# end function

"""
Name:           list_courses
Purpose:        This function will display the list of courses within the candidates 
                transcript.
Argument:       The function accepts a list called transcript (the candidates transcript).
Returns:        The function does not return a value.
"""

def list_courses (course_list: list) -> None:

    print ("      Course     Semester     Grade")
    
    line_number = 0
    
    for course in course_list:
        line_number += 1
        print(line_number, course)
    # end iteration
        
# end function

"""
Name:           update_course
Purpose:        This function will update a specific course based on user input. 
                By prompting the user to choose which course to update, this function
                will allow the user to update the semester and grade values of 
                the specific course.
Argument:       The function accepts a list called transcript (the candidates transcript).
Returns:        The function does not return a value.
"""


def update_course( transcript : list ) -> None:
    """
    Import validation functions for semester & grade. This ensures that the input
    value from the user is formatted correctly without having to validate it 
    within this file.
    """
    from validations import validate_semester, validate_grade
    
    # We will present the user with a List of Course objects
    list_courses(transcript)
    
    # Prompt for which course object to update
    index = int(input("By number, which course do you want to update?: "))
    
    # The if statement is used to ensure the course exists within the transcript.
    if (index <= len(transcript)) and ( index > 0):
        
        """
        Since the user may not be aware that the language starts counting at 0,
        we incorporate the following two lines to make sure that the value the
        user inputs corresponds to the value attached to the course.
        """
        index -= 1
        target = transcript[index]
        
        update_OK = True
        
        """ The if statements prompts the user to input the new semester/grade value,
        while also validating the format of the input. The function will update
        the course if format is correct. """
        
        new_semester = input("Enter the correct semester: ")
        if validate_semester(new_semester) == False:
            update_OK = False
        # end selection
        
        new_grade = input("Enter the correct grade: ")
        if validate_grade(new_grade) == False:
            update_OK = False
        # end selection
        
        # The if statement updates the course if the OK value is true. 
        if update_OK == True:
            # Do the update
            target.set_crs_semester(new_semester)
            target.set_crs_grade(new_grade)
            
            print("Update successful.")
        
        # If the OK value is false, the functions tells the user. 
        else:
            print("Some of your data is invalid. Update canceled.")
    
    
    # If the inputted value is not within the range of the transcript, the function tells the user. 
    else:
        print("I am sorry, that Course does not exist. ")
        
    # end selection
# end function

"""
Name:           calculate_GPA
Purpose:        This function will calculate the user's GPA using their 
                transcript information. 
Argument:       The function accepts a list called transcript (the candidates transcript).
Returns:        The function returns a float value.
"""

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
        the course code. The last digit of the course code signifies the hours
        counted for the class. 
        """
        hours = int(course.get_crs_code()[ -1 ])
        
        #Calculate Quality Points; done by grabbing the instances of the grades
        pts = quality_points[ course.get_crs_grade()] * hours
        
        #Accummulate
        
        total_hours += hours
        total_points += pts
        # end iteration
# end function
    
    #Calculating and returning the candidates GPA
    return total_points / total_hours
# end function

"""
Name:           transcript_driver
Purpose:        This function acts as the driver for the whole application.  
                It prompts the user to input a value that corresponds with 
                an option. And if that value exists, it will run the option that
                was selected.
Argument:       The function accepts a list called transcript (the candidates transcript).
Returns:        The function does not return a value.
"""

def transcript_driver() -> None:
    import pickle
    
    print("\n\n")
    print("Welcome to the Transcript Application \n\n")
    
    """
    We need to start by asking if the User already HAS a Transcript file.
    If not, we need to create one...
    """
    response = input("Do you have an existing Transcript file? Yes or No.  ")
    
    if response == "Yes":
        # The transcript file already exists
        # Get the file information from the User.
        file_name = input("Please identify the file containing your Transcript:  ")
        
        # Using the pickle library to read and load the bytes into the transcript variable
        with open ( file_name, 'rb') as in_file:
            transcript = pickle.load(in_file)
        # end context
        
    else:
        # We need to BUILD a List with 1 or more Course objects
        
        transcript = list()
        
        #   By ensuring that the user adds a course, make sure a value is "yes"
        # and incorporate a while loop to prompt the user to add a course
        add_one = 'Yes'
        while add_one == 'Yes':
            add_course(transcript)
            add_one = input("Do you wish to add another Course? Yes or No. ")
            
        # end iteration
    
    # end selection    
    
    # Setting a default option
    option = 1
    
    # Making sure the option chosen by the user exists in the selection list
    while (option > 0) and (option < 5):
            
        option = select_option()
        if (option == 1):
                # If the user chooses one, the add_course function will run
                add_course(transcript)
        elif (option == 2):
            # If the user chooses one, the list_course function will run
                list_courses(transcript)
        elif (option == 3):
            # If the user chooses one, the update_course function will run
                update_course(transcript)
        elif (option == 4):
            # If the user chooses one, the calculate_GPA function will run
            print("Calculating...")
            gpa = calculate_GPA(transcript)
            print("Your current GPA is %.2f \n" % gpa)
                
        elif (option == 5):
            # This option ensures that the user's transcript file is saved and
            # will exit the application afterwards.
            
            file_name = input("Please provide a name for your Transcript file: ")
            with open(file_name, 'wb') as out_file: 
                pickle.dump(transcript, out_file, pickle.HIGHEST_PROTOCOL)
                
                # end context
                
            print("Your Transcript file has been saved.")
            print("Goodbye!")
                
        else:
            option = 1
            print("That is not a valid option. Please try again. ")
            # end selection      
    # end iteration    
# end driver

"""
Name:           select_option
Purpose:        This function presents a list of options given to the user 
                to choose from.  
Argument:       The function does not accept any arguments.
Returns:        The function returns an integer value.
"""

def select_option() -> int:
    
    # Present the menu to the User
    print("\n\n")
    print("What would you like to do next?")
    print("1. Add another Course")
    print("2. List my Courses")
    print("3. Update a Course")
    print("4. Calculate my GPA")
    print("5. Exit the application")
    
    
    # Prompt the User for selection
    option = int(input("Select your option by number:  "))
    return option
# end select_option/function

#==============================================================================
"""
Now, we just have to execute the application
"""

transcript_driver()
 