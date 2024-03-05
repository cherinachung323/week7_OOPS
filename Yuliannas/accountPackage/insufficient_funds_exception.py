# Defines the InsufficientFundsException class, which inherits from the Exception class.
# By inheriting from Exception,InsufficientFundsException becomes a type of exception that can be raised in programs.
class InsufficientFundsException(Exception):
    # defines the constructor method for the InsufficientFundsException class. The constructor takes an optional message
    # parameter, which defaults to "Insufficient funds". This message will be used to provide additional information
    # when the exception is raised.
    def __init__(self, message="Insufficient funds"):
        # assigns the value of the message parameter to the message attribute of the InsufficientFundsException instance.
        self.message = message
        # calls the constructor of the superclass (Exception) using super(). It passes the message attribute as the
        # argument to initialise the exception message. This ensures that the message passed to the
        # InsufficientFundsException constructor is used to set the error message for the exception.
        super().__init__(self.message)
