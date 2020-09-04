#!/path/to/env/bin/python

from restore import backup
from upload import DirectoryClient
import time
import datetime
from datetime import date, timedelta
import threading
import os
import shutil

def main():
    DATE = time.strftime('%Y-%m-%d') #string date
    TIME = (datetime.datetime.utcnow().time()).strftime('%H:%M:%S')
    yesterday = date.today() - timedelta(days=1) # to remove folders from yesterday
    yes_DATE = yesterday.strftime('%Y-%m-%d')

    folderpath = os.path.join("/path/to/dir/backup", DATE)
    old_path = os.path.join("/path/to/dir/backup", yes_DATE)
    
    if os.path.exists(old_path): # remove dir from day before
        shutil.rmtree(old_path)

    if not os.path.exists(folderpath): # create path if not already exists
        os.makedirs(folderpath, exist_ok=True)

    # getting all together
    backup(TIME, folderpath)
    client = DirectoryClient("DefaultEndpointsProtocol=<azureConnectionString>", '<containerName>')
    client.upload('/path/to/dir/backup/'+DATE, '')
