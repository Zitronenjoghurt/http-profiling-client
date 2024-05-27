class ApiResponse():
    def __init__(self, status: int, content: str) -> None:
        self.status = status
        self.content = content