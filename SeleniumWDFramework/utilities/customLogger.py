import inspect
import logging


def customlogger(loglevel=logging.DEBUG):
    loggername = inspect.stack()[1][3]
    # This method will provide the name or class calling this method
    logger = logging.getLogger(loggername)

    # setting the default level for the logger

    logger.setLevel(logging.DEBUG)

    # setting up the file handler and what ever file we will be creating will use the logname
    filehandler = logging.FileHandler("automation.log", mode='a')

    # setting the level of filehandler
    filehandler.setLevel(loglevel)

    # formating the file
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%Y , %H:%M:%S , %p')

    # adding the formater to the file handler
    filehandler.setFormatter(formatter)

    # adding the file handler to the logger
    logger.addHandler(filehandler)

    return logger
