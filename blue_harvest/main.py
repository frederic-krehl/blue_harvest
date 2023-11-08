# --------------------------------------------------------------------------------------------------#
# Initialization and parsing arguments


import pandas as pd
from blue_harvest import general_functions
import numpy as np
import time
from hashlib import md5
import requests as rq
import json

args, unknown = general_functions.initiate_parser().parse_known_args()
logger = general_functions.initiate_logger(args)

# display settings for pandas
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',18)

z1_path = general_functions.get_d_env_vars()['z1_path']

# END Initialization and parsing arguments
#--------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------#
# get data

def get_100_characters(offset=0):
    public_key = general_functions.get_d_env_vars()['public_key']
    private_key = general_functions.get_d_env_vars()['private_key']
    ts = str(time.time())
    hash_str = md5(f"{ts}{private_key}{public_key}".encode("utf8")).hexdigest()

    params = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash_str,
        "limit": 100,
        "offset": offset,
    }
    try:
        r = rq.get('http://gateway.marvel.com/v1/public/characters', params=params)
    except Exception as e:
        return False, e
    else:
        #fetch relevant data into df
        d = r.json()
        df = pd.DataFrame(d['data']['results'])
        df = df[['name','comics']]
        df['Quantity of comics'] = df['comics'].apply(lambda x: x['available'])
        #cleanup
        df.rename(columns={'name':'Character name'}, inplace=True)
        df.drop(columns=['comics'], inplace=True)
        logger.debug("fetched next 100 rows")
    return df


def get_characters(): # get all characters
    logger.debug("Starting to fetch characters + comics")
    df = pd.DataFrame()
    for i in range(0, 16): # total of 1563 characters, i.e. 16 *100

        df_temp = get_100_characters(offset=i*100)
        df = pd.concat([df, df_temp], ignore_index=True)

    df.to_excel(z1_path + 'characters.xlsx', index=False)
    logger.debug("outputfile 'characters.xlsx' created")


get_characters()
