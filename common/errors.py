class CompileError(Exception):
    pass

class CompileException(Exception):
    pass

class NameConflictError(CompileError):
    pass

class ObjectAlreadyDefinedException(CompileException):
    """
    Exception raised when the same object is defined in the same scope under the same name a second time.
    This should happen when module items are registered in the global pass and then resolved, in which case
    it can be caught and ignored.
    """
    pass