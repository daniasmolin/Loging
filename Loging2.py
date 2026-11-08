import logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s")

try:

    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Сталася помилка під час виконання операції:")