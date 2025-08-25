import sys
from networksecurity.logging import logger

# Defining a custom exception class for the project
class NetworkSecurityException(Exception):
    # Constructor method that accepts the error message and system exception details
    def __init__(self, error_message, error_details: sys):
        # Store the original error message
        self.error_message = error_message
        
        # Unpack the exception information using sys.exc_info()
        # This returns a tuple: (type, value, traceback)
        _, _, exc_tb = error_details.exc_info()

        # Get the line number where the exception occurred
        self.lineno = exc_tb.tb_lineno

        # Get the filename of the script where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    # Define string representation for printing/logging the exception
    def __str__(self):
        return "Error occurred in python script name[{0}] line number [{1}] error message[{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )

# This block only runs if the script is executed directly (not when imported)
if __name__ == "__main__":
    try:
        # Intentionally causing a division-by-zero error to demonstrate custom exception handling
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        # Raising our custom exception and passing the original exception and sys module for traceback
        raise NetworkSecurityException(e, sys)