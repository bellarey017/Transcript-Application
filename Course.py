
class Course:
    
    def __init__( self,         
                  code: str,       
                  semester: str,
                  grade: str ):    

        self.set_crs_code( code )
        self.set_crs_semester( semester )
        self.set_crs_grade( grade )

    
    """
        Name:        set_crs_code
        Function:    Mutator method for crs_code instance variable
        Arguments:   A string value to assigne to crs_code
        Returns:     No value returned
    """
    def set_crs_code( self,       
                      code: str ) -> None:
        self.crs_code = code
    
    """
        Name:        set_crs_semester
        Function:    Mutator method for crs_semester instance variable
        Arguments:   A string value to assigne to crs_semester
        Returns:     No value returned
    """
    def set_crs_semester( self,
                          semester: str ) -> None:
        self.crs_semester = semester
    
    """
        Name:        set_crs_grade
        Function:    Mutator method for crs_grade instance variable
        Arguments:   A string value to assigne to crs_grade
        Returns:     No value returned
    """
    
    def set_crs_grade( self,
                       grade: str ) -> None:
        self.crs_grade = grade

    
    """
        Name:        get_crs_code
        Function:    Accessor method for crs_code instance variable
        Arguments:   None
        Returns:     Value of crs_code
    """
    def get_crs_code( self ) -> str:
        return self.crs_code
    
    """
        Name:        get_crs_semester
        Function:    Accessor method for crs_semester instance variable
        Arguments:   None
        Returns:     Value of crs_semester
    """
    def get_crs_semester( self ) -> str:
        return self.crs_semester
    
    """
        Name:        get_crs_grade
        Function:    Accessor method for crs_grade instance variable
        Arguments:   None
        Returns:     Value of crs_grade
    """
    def get_crs_grade( self ) -> str:
        return self.crs_grade
    
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
    
        
