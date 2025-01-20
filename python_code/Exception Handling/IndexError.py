# IndexError: list index out of range
# IndexError is raised when you try to access an index that is outside the range of the list.
# In the below code, we have a list of members and we are trying to access the 4th element of the list which is not present. Hence, it will raise an IndexError.

import sys

class Join:
    '''
    This is Join Class
    '''
    def __init__(self):
        '''
        This is Constructor
        '''
        print('Constructor')
    
    def welcome(self):
        '''
        This is Welcome Method
        '''
        print('Welcome Method')
    
    def __del__(self):
        '''
        This is Destructor
        '''
        print('Destructor')
    
    def members(self):
        '''
        This is members method
        '''
        members = ['John','Smith','David']
        print(members[2])
        try:
            print(members[2])
        except IndexError as e:
            error_info = sys.exc_info()
            print('Error Info:',error_info)
            print(error_info[0], ': ', error_info[1])
            print('Index Error occurred:',e)
        except IOError as ioe:
            print('Exception occurred in members method', ioe)
        except ImportError as impe:
            print('Exception occurred in members method', impe)
        else:
            # This block will execute if there is no exception and try block is executed successfully
            print('All the members are printed successfully')
        finally:
            # This block will execute irrespective of exception occurred or not
            print('Finally block executed')



j1 = Join()
j1.welcome()
j1.members()
