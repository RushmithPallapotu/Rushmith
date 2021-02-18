import logging

import pytest


@pytest.mark.usefixtures("browserinvo")
class Baseclass():

    def loggerinfo(self):

        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)

        return logger


