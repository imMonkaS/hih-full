class AppException(Exception):
    msg: str | None = NotImplemented
    error_code = 1
    status_code: int = NotImplemented
    system_prefix: str | None = NotImplemented

    def __init__(self, msg=''):
        super().__init__()
        self.msg = msg or self.msg

    def __str__(self):
        return self.msg or self.__doc__ or self.__class__.__name__

    def __call__(self):
        return str(self)


class UnknownException(AppException):
    system_prefix = 'APP'
    msg = 'Service error'
    error_code = 1
    status_code = 500
