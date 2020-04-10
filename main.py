from lib.utils import compute_laziest_path
import argparse
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--number', help="Example: ptyhon main.py --number 110", default = '110')
  args = parser.parse_args()


  resp = compute_laziest_path(args.number)
  print(resp)
