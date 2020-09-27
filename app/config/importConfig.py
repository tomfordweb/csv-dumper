class ImportConfig:
    """<Config(prefix="us")>"""
    def __init__(self, **kwargs):
        self.prefix = None
        allowedKeys = set(['prefix'])
        # Set provided values
        self.__dict__.update((key,value) for key, value in kwargs.items() if key in allowedKeys)
