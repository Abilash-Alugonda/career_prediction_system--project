

class UserManagementError(Exception):
    pass


class ValidationError(UserManagementError):
    pass


class DuplicateUserError(UserManagementError):
    pass


class InvalidLoginError(UserManagementError):
    pass


class InvalidProfileError(UserManagementError):
    pass


class FileHandlingError(UserManagementError):
    pass