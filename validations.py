""" 
This script contains validation functions for the instance values offered
to the Course class description/construtor.
"""

"""
Name:           validate_grade
Purpose:        This function will validate a string offered as
                   candidate grade prior to sending to the course constructor.
                   It will return a boolean value indicating validity.
Argument:       The function accepts one string as a candidate grade.
Returns:        The function returns a boolean value indicating validity.
"""

def validate_grade(grade : str) -> bool:
    valid_grades = [ 'A+', 'A', 'A-',
                    'B+', 'B', 'B-',
                    'C+', 'C', 'C-',
                    'D+', 'D', 'D-',
                    'F']
    if grade in valid_grades:
        response = True
    else:
        response = False
        
    return response


"""
Name:           validate_code
Purpose:        This function will validate a string offered as
                   the code of a class prior to sending to the course constructor.
                   It will return a boolean value indicating validity.
Argument:       The function accepts one string as a course code.
Returns:        The function returns a boolean value indicating validity.
"""


def validate_code (code : str) -> bool:
    import re         # Import RegEx Library
    
    """ Beginning with the very first string (^), within the range of A-Z, you
    have to have at minimum 2 letters, and at most 4 letters. Then ensure that 
    there is exactly 4 digits and nothing else trailing after that. ($)
    """
    valid_code = re.compile("^[A-Z]{2,4}\d{4}$")
    
    """
    The matcher variable is essentially using the "code" input and running it
    through the regex to ensure that it matches the specific constraints.
    The regex then creates an object, if it matches, as matcher and depending on
    if an object is created or not, the function will return the boolean variable.
    This will also occur in the function validate_semester, but with different
    constraints.
    """

    matcher = valid_code.match(code)
    
    if matcher == None:
        result = False
    else:
        result = True
        
    return result

"""
Name:           validate_semester
Purpose:        This function will validate a string that describes the semester
                that the candidate took this class prior to sending to the course 
                constructor. It will return a boolean value indicating validity.
Argument:       The function accepts one string as a course code.
Returns:        The function returns a boolean value indicating validity.
"""

def validate_semester (semester : str) -> bool:
    import re         # Import RegEx Library
    
    """ Beginning with the very first string (^), within the range of the units 
    'Fall, Spring, Summer', you look for a space (denoted as an actual space),
     Then ensure that the next two digits start with '20' and any two digits after
     by using \d{2}. Then make sure nothing else is trailing after that. ($)
    """
    valid_semester = re.compile("^(Fall|Spring|Summer) 20\d{2}$")
    
    matcher = valid_semester.match(semester)
    
    # Based on the outcome of matcher, the result variable will hold a boolean
    # value that corresponds with the validity of the input. This boolean value 
    # will then be returned to the caller (wherever the function was used).
    
    if matcher == None:
        result = False
    else:
        result = True
        
    return result











