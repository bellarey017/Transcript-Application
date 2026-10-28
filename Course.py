# -*- coding: utf-8 -*-
"""
(C) 2024, Terri Davis

    This code describes the Course class.
    
    ATTRIBUTES:  Course Code (6-7 alphanumeric characters)
                 Semester (Up to 11 alphanumeric characters)
                 Grade (One or two alphanumeric characters)

    OPERATIONS:  Standard MUTATOR and ACCESSOR methods
                 String method to provide a "state report" of object

"""


class Course:
    
    """
        Constructor
        
        Python, unlike Java, does not permit the overloading of methods/
        functions. Therefore there can be ONLY ONE constructor in a Python 
        class.
        
        The constructor's name is fixed - that is, determined by the language -
        and must meet that requirement.
        
        Note: It is possible to create a constructor that could fill the role
        of (Java style) multiple constructors. It requires much more design 
        work and code to accomplish...
    """
    
    def __init__( self,             # ALL CLASS FUNCTIONS require "self" as 
                  code: str,        #  the first argument
                  semester: str,
                  grade: str ):     # NOTE that we are specifying type for args

        self.set_crs_code( code )
        self.set_crs_semester( semester )
        self.set_crs_grade( grade )
        
    # end CONSTRUCTOR
    
    """
        Standard MUTATOR methods:
            Course Code
            Semester
            Grade
    """
    
    """
        Name:        set_crs_code
        Function:    Mutator method for crs_code instance variable
        Arguments:   A string value to assigne to crs_code
        Returns:     No value returned
    """
    def set_crs_code( self,       # The notation style below provides for 
                      code: str ) -> None:   # self-documentation
        self.crs_code = code
    # end crs_code mutator
    
    """
        Name:        set_crs_semester
        Function:    Mutator method for crs_semester instance variable
        Arguments:   A string value to assigne to crs_semester
        Returns:     No value returned
    """
    def set_crs_semester( self,
                          semester: str ) -> None:
        self.crs_semester = semester
    # end crs_semester mutator
    
    """
        Name:        set_crs_grade
        Function:    Mutator method for crs_grade instance variable
        Arguments:   A string value to assigne to crs_grade
        Returns:     No value returned
    """
    
    def set_crs_grade( self,
                       grade: str ) -> None:
        self.crs_grade = grade
    # end crs_grade mutator

    
    """
        Standard ACCESSOR methods:
            Course Code
            Semester
            Grade
    """    
    
    """
        Name:        get_crs_code
        Function:    Accessor method for crs_code instance variable
        Arguments:   None
        Returns:     Value of crs_code
    """
    def get_crs_code( self ) -> str:
        return self.crs_code
    # end crs_code accessor 
    
    """
        Name:        get_crs_semester
        Function:    Accessor method for crs_semester instance variable
        Arguments:   None
        Returns:     Value of crs_semester
    """
    def get_crs_semester( self ) -> str:
        return self.crs_semester
    # end crs_semester accessor   
    
    """
        Name:        get_crs_grade
        Function:    Accessor method for crs_grade instance variable
        Arguments:   None
        Returns:     Value of crs_grade
    """
    def get_crs_grade( self ) -> str:
        return self.crs_grade
    # end crs_grade accessor
    
    
    
    """
        This is the equivalent of a toString method in Java.
        It produces a "state report" for the object.
    """
    
    """
        Name:        __str__
        Function:    State report - returns all instance variable values in a
                     formatted string object
        Arguments:   None
        Returns:     A formatted string object
    """    
    def __str__( self ) -> str:
        course = self.get_crs_code( )
        semester = self.get_crs_semester( )
        grade = self.get_crs_grade( )
        
        out_str = "    {:<8}\t{:<12}\t{:<2}"
        
        return out_str.format( course,
                               semester,
                               grade )
    # end __str__ (toString // state report)
    
# end CLASS DEFINITION of Course
        