class EncodeObject:
    """
    Class that holds parameters for performing encoding. For now, it holds, image and message.
    Can include other parameters in the future in case we need to include more features and send more params.
    """
    def __init__(self, image, message):
        self.image = image
        self.message = message

