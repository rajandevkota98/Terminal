import logging
logging.basicConfig(filename='test4.log', level=logging.WARNING, format='%(asctime)s  %(levelname)s  %(message)s')

try:
    logging.critical('I am trying to read a file')
    with open('raj.txt',"r"):
        logging.info("sucessfully done")
except Exception as e:
    logging.error(e)
    logging.exception(e)