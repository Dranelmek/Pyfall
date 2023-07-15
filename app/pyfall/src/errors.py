class ApiError(Exception):
    '''
    Custom ApiError exception class for raising an error 
    for when the api returns an error object
    '''

    def __init__(self, value):
        self.value = value