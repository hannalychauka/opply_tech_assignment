class ChoiceEnum(object):
    """
    Base enum class. Use uppercase by convention.

    Sample of usage:
        class StatusesEnum(ChoiceEnum):
            NEW = 0
            APPROVED = 1
    """
    messages = {}

    @classmethod
    def for_choice(cls):
        return [(v, k) for k, v in cls.__dict__.items() if k.isupper()]

    @classmethod
    def values(cls):
        return [v for k, v in cls.__dict__.items() if k.isupper()]