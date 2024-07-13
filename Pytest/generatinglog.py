import logging

logging.basicConfig(filename="..\\Logs\\logfile.log",format='%(asctime)s: %(levelname)s',level=logging.INFO)

log = logging.getLogger()

log.info(msg='Hello')