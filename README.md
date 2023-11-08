#######################

1. Install the required dependencies in an virtual environment:

- install poetry on your machine
- run "poetry install" in the project directory

2. Handle your credentials from marvel

- generate your own public key and private key from marvel
- save them in the folder where you want to save the output file
- the filetype should be csv
- the filefomat should be <public_key,private_key> (example: 123456789,123456789)

3. To run the program, type:

- python3 main.py -p <path_to_folder_where_to_save_the_output> (example: python3 main.py -p 'C:blue_harvest\\')

