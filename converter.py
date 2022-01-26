import glob
import re
import subprocess
from multiprocessing.dummy import Pool

# Convert .xlsx to .csv for speed improvement
xlsx_path = 'xlsx-forsale/'
csv_path = 'csv-forsale/'
list_of_xlsx = glob.glob(xlsx_path+'*.xlsx')

# Use regex to only grab .xlsx files in directory
commands = []
for filepath in glob.glob(xlsx_path+'*.xlsx'):
    filename = re.search(r'(.+[\\|\/])(.+)(\.(csv|xlsx|xlx))', filepath) #Extract File Name on group 2 "(.+)"

    call = ["python", "venv/bin/xlsx2csv", filepath, csv_path+'{}.csv'.format(filename.group(2))]
    commands.append(call)

pool = Pool(2) # Specify How many concurrent threads

# Use functools.partial(subprocess.call, shell=True) in place of subprocess.call if you're on windows
for i, return_code in enumerate(pool.imap(subprocess.call, commands)):
    if return_code != 0:
        print("Command # {} failed with return code {}.".format(i, return_code))

