import sys
import traceback
from industrial_safety_monitoring.logger import get_logger

logger = get_logger(__name__)


def get_detailed_error_message(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error message including file name and line number
    """
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"

    return f"""
Error occurred in script: [{file_name}]
Line number: [{line_number}]
Error message: [{str(error)}]
"""


class CustomException(Exception):
    def __init__(self, error: Exception, error_detail: sys):
        super().__init__(str(error))

        self.error_message = get_detailed_error_message(error, error_detail)

        # Log immediately (important in production)
        logger.error(self.error_message)

    def __str__(self):
        return self.error_message


# Testing
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException(e, sys) from e