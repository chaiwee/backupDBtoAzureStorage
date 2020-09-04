import os
import pipes

def backup(TIME, folderpath):

    print('back-uping.....')

    host = 'localhost'
    user = 'root'
    password = 'password'
    db = 'database1'

    saved_file = TIME + '-' +db + '.sql'

    dumpcmd = "mysqldump -h " + host + " -u " + user + " -p"+ password +" " +db + " > " + pipes.quote(folderpath) + "/"+ saved_file
    os.system(dumpcmd)

    with open("backup.log", "a") as f:
        f.write("Backup script completed\n")
        f.write("Your backups have been created in '"+ folderpath + "' directory\n")
    
