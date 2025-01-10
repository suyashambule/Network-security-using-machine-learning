import sys


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in python [{0}] line number [{1}] error message [{2}]".format(self.file_name, self.lineno, self.error_message)

if __name__ == '__main__':
    try:
        a = 1 / 0  # This will cause a ZeroDivisionError
        print('This should not be printed')
    except Exception as e:
        logger.error(f"Exception occurred: {e}")  # Log the exception
        raise NetworkSecurityException(e, sys)  # Raise custom exception with traceback details
