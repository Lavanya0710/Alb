import logging
class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs\\automation.log",format='%(asctime)s: %(levelname)s: %(message)s',force=True, datefmt='%d-%m-%Y %I:%M:%S %p')
        logging.basicConfig(filename="C:\\Users\\getma\\PycharmProjects\\Alb\Logs\\automation.log", format='%(asctime)s: %(levelname)s: %(message)s', force=True, datefmt='%d-%m-%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger

