class LibraryError(Exception):
    """Base class for all business error in this app library exceptions."""

class NotFoundError(LibraryError):
    """Something was looked up and does not exist."""

class ConflictError(LibraryError):
    """The request fight with the current state (duplicate ,limit reached)"""