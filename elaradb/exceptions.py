# Add all custom exception classes here 

class SomeRandomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Error -> {self.message}'