class UnknownTld(Exception):
    pass


class FailedParsingWhoisOutput(Exception):
    pass


class DomainNotFound(Exception):
    pass


class UnknownDateFormat(Exception):
    pass


class WhoisCommandFailed(Exception):
    pass
