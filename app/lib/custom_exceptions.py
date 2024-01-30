DEFAULT_ERROR_MESSAGE = 'An Unexcepted error has occured'


class DuplicateRecordException(Exception):
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class CreateRecordFailedException(Exception):
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class ForbiddenException(Exception):
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
