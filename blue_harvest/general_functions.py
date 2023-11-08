
import logging
import argparse
import os

#--------------------------------------------------------------------------------------------------#

def initiate_parser():
    "# Parse Args & Assign user specific parameters"
    parser = argparse.ArgumentParser(
        description='parses arguments, such as --dev-ops-environment',
        epilog="")
    parser.add_argument(
        '-p','--path', help = 'folder with private key and where output should be saved', required=False, default=False )
    return parser

#--------------------------------------------------------------------------------------------------#



#--------------------------------------------------------------------------------------------------#

def initiate_logger(args, level = "DEBUG"):
    "logging"
    #Logger: create logger
    logger = logging.getLogger('dev_logger')
    logger.propagate = False
    logger.setLevel(level)

    # Logger: create console handler with a higher log level
    stream_handler = logging.StreamHandler()

    if level == "DEBUG":
        stream_handler.setLevel(logging.DEBUG)
    else:
        stream_handler.setLevel(logging.INFO)

    # Logger: create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | \n %(message)s ')
    stream_handler.setFormatter(formatter)
    # Logger: add the handlers to the logger
    logger.addHandler(stream_handler)
    return logger

#--------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------#
def get_d_env_vars():
    args, unknown = initiate_parser().parse_known_args()
    d_env_vars = {}
    run_on_prod = True
    if args.path is not False:
        d_env_vars['z1_path'] = args.path
        d_env_vars['z2_path'] = args.path
        d_env_vars['z3_path'] = args.path

    if os.getlogin() == 'WTS84188':
        d_env_vars['z1_path'] = r'C:\blue_harvest\z1_extraction\\'
        d_env_vars['z2_path'] = r'C:\blue_harvest\z2_core\\'
        d_env_vars['z3_path'] = r'C:\blue_harvest\z3_loading\\'
        # get keys from csv file
        keys = open(d_env_vars['z1_path'] + '\key.csv', 'r').read().split(',')
        d_env_vars['public_key'] = keys[0]
        d_env_vars['private_key'] = keys[1]
    # other users here


    return d_env_vars
