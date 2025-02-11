import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in Python Script name [{0}] Line No. [{1}] Error Message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message

class customException(Exception):

    # Constructor or Initializer
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    # __str__ is to print() the value
    def __str__(self):
        return self.error_message


if __name__ == "__main__":

    try:
        a=1/0
        
    except Exception as e:
        logging.info("can't devide by zero")
        raise customException('Division by zero', error_detail=sys)