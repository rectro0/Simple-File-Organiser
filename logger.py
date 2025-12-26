import logging


logging.basicConfig(level= logging.warning , filename= "log.log" , filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.warning("warning") 