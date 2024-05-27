import logging

class LC:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREY = '\033[90m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class FileFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: f"%(asctime)s %(levelname)s    %(name)s %(message)s",
        logging.INFO: f"%(asctime)s %(levelname)s     %(name)s %(message)s",
        logging.WARNING: f"%(asctime)s %(levelname)s  %(name)s %(message)s",
        logging.ERROR: f"%(asctime)s %(levelname)s    %(name)s %(message)s",
        logging.CRITICAL: f"%(asctime)s %(levelname)s %(name)s %(message)s"
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

class ColoredFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: f"{LC.GREY}{LC.BOLD}%(asctime)s{LC.ENDC} {LC.CYAN}{LC.BOLD}%(levelname)s{LC.ENDC}    %(name)s %(message)s",
        logging.INFO: f"{LC.GREY}{LC.BOLD}%(asctime)s{LC.ENDC} {LC.BLUE}{LC.BOLD}%(levelname)s{LC.ENDC}     %(name)s {LC.BLUE}%(message)s",
        logging.WARNING: f"{LC.GREY}{LC.BOLD}%(asctime)s{LC.ENDC} {LC.YELLOW}{LC.BOLD}%(levelname)s{LC.ENDC}  %(name)s {LC.YELLOW}%(message)s",
        logging.ERROR: f"{LC.GREY}{LC.BOLD}%(asctime)s{LC.ENDC} {LC.RED}{LC.BOLD}%(levelname)s{LC.ENDC}    %(name)s {LC.RED}%(message)s",
        logging.CRITICAL: f"{LC.GREY}{LC.BOLD}%(asctime)s{LC.ENDC} {LC.RED}{LC.BOLD}%(levelname)s %(name)s %(message)s"
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

class APILogger:
    def __init__(self):
        self.logger = logging.getLogger("API")
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('api.log')
        stream_handler = logging.StreamHandler()

        file_handler.setLevel(logging.DEBUG)
        stream_handler.setLevel(logging.INFO)

        file_handler.setFormatter(FileFormatter())
        stream_handler.setFormatter(ColoredFormatter())

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger
    
    def api_request(self, method: str, url: str, status: int, content: str):
        self.logger.debug(f"[{status}] {method} {url}: {content}")

LOGGER = APILogger()