
class GeminiError(Exception):
    """
    Error caused under Gemini module
    """

    def __init__(self, message):
        super().__init__(message)
