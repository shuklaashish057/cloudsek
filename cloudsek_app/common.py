class ValidationError(Exception):
    def __init__(self, msg):
        print('hello')
        self.msg = msg


class ApplicationError(Exception):
    def __init__(self, msg):
        self.msg = msg


class TTSClientError(Exception):
    def __init__(self, status_code, msg):
        self.status_code = status_code
        self.msg = msg
