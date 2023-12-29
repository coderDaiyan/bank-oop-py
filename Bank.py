class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self._total_loan = 0
        self.loanAvailable = True
        self._balance = 0
        self._users = []
        self._admins = []