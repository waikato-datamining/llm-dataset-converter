import abc

from ldc.core import CommandlineHandler, LOGGING_WARN


class Downloader(CommandlineHandler, abc.ABC):
    """
    Base class for downloader classes.
    """

    def __init__(self, logging_level: str = LOGGING_WARN):
        """
        Initializes the handler.

        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logging_level=logging_level)

    def download(self):
        """
        Performs the download.
        """
        raise NotImplementedError()