# -*- coding: utf-8 -*-
import logging
import getopt , sys
from golf_project.rounds import rounds

logger = logging.getLogger(__name__)


# FIXME: put actual code here
def example():
    logger.info('Providing information about the excecution of the function.')



def main(argv): 
    try: 
        opts , args = getopt.getopt(argv , "r:" , "ronda=") 

    except getopt.GetoptError as err:
        print (err)
        print ("Usage : golf_project.py -r <round>")
        sys.exit(2)

    for option,arg in opts: 
        if option in ("-r" , "--ronda"): 
            date = arg 
        else: 
            assert False 
    
    rounds.get_fixture_data(date)

if __name__ == "__main__" : 
    main(sys.argv[1:])