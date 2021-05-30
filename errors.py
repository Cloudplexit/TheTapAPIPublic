class PrimaryServerException(Exception):
    """Exception raised for errors in primary server.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
