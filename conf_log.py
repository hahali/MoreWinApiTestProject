import logging

logging.basicConfig(filename='runlog.log',level=logging.DEBUG,
                  format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

logging.basicConfig(level=logging.INFO)
logging.debug("debug info")
logging.info("info")
logging.warning("warning info")
logging.error("error info")
logging.critical("critical info")