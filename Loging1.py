import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.info(datetime.date.today().strftime("%Y-%m-%d"))