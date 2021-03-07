import env
import logging
import sys


logging.basicConfig(stream=sys.stdout, level=env.log_level, format='%(asctime)s | %(levelname)s | %(message)s')