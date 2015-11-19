import os
import time
import datetime
import fs             # Install by `pip install pyfs`
import re

ROOT_DIR = fs.home()
MONITORING_ROOT_DIR = 'Dropbox/'
TARGET_ROOT_DIR = 'Dropbox/_Archives'
LOG_DIR = 'Dropbox/_Archives/Log'
BACKUP_DIR_SUFFIX = '_archives'
ELAPSED_TIME = 7776000  #7776000 seconds = 90 days

def _remove_test_dir(ROOT_DIR, TARGET_ROOT_DIR, backup_dir_name):
    backup_dir_name = fs.join([ROOT_DIR, TARGET_ROOT_DIR, backup_dir_name])
    try:
        fs.rmdir(backup_dir_name, recursive=True)
        print (backup_dir_name, "was successfully removed")
    except:
        print ("ERROR", backup_dir_name, "couldn't removed by func:_remove_test_dir")

def get_monitoring_dir(ROOT_DIR, MONITORING_ROOT_DIR):
    return fs.join([ROOT_DIR, MONITORING_ROOT_DIR])

def get_backup_dir_list(monitoring_dir, ELAPSED_TIME):
    backup_dir_list = []
    now = int(time.time())
    for f in fs.find('*', path=monitoring_dir):
        last_accessed = fs.stat(f).st_atime
        diff = now - last_accessed
        if diff > ELAPSED_TIME:
            if not fs.dirname(f) in backup_dir_list:
                backup_dir_list.append(fs.dirname(f))
    return list(set(backup_dir_list))

def should_create_archive(backup_dir_list):
    return True if len(backup_dir_list) >=0 else False

def get_backup_dir_name(BACKUP_DIR_SUFFIX):
    today_obj = datetime.datetime.today()
    today_str = str(today_obj.year)+str(today_obj.month)+str(today_obj.day)
    backup_dir_name = today_str + BACKUP_DIR_SUFFIX
    return backup_dir_name

def create_new_backup_root_dir(ROOT_DIR, TARGET_ROOT_DIR, backup_dir_name):
    backup_dir_path = fs.join([ROOT_DIR, TARGET_ROOT_DIR, backup_dir_name])
    if not fs.exists(backup_dir_path):
        try:
            fs.mkdir(backup_dir_path)
            print (backup_dir_path, "was successfully created")
        except:
            print ("Cant create a backup directory in func: create_new_backup_root_dir")


def create_archive_tree(monitoring_dir, ROOT_DIR, TARGET_ROOT_DIR, backup_dir_name, backup_dir_list):
    for source_full_path in backup_dir_list:
        re_pattern = re.compile(r'%s' % monitoring_dir)
        source_path = re.sub(re_pattern, '', source_full_path)
        archive_path = fs.join([ROOT_DIR, TARGET_ROOT_DIR, backup_dir_name, source_path])
        if not fs.exists(archive_path):
            try:
                fs.mkdir(archive_path)
            except:
                print (archive_path, "Can't create archive tree in func: create_archive_tree")

def get_backup_file_list(monitoring_dir, ELAPSED_TIME):
    backup_file_list = []
    now = int(time.time())
    for f in fs.find('*', path=monitoring_dir):
        last_accessed = fs.stat(f).st_atime
        diff = now - last_accessed
        if diff > ELAPSED_TIME:
            backup_file_list.append(f)
    return backup_file_list

def export_neglected_file_list(monitoring_dir, ROOT_DIR, LOG_DIR, backup_file_list):
    today_obj = datetime.datetime.today()
    today_str = str(today_obj.year)+str(today_obj.month)+str(today_obj.day)
    export_name = today_str + "_neglected_files.log"
    export_path = fs.join([ROOT_DIR, LOG_DIR, export_name])
    if not fs.exists(fs.join([ROOT_DIR, LOG_DIR])):
        try:
            fs.mkdir(fs.join([ROOT_DIR, LOG_DIR]))
        except:
            print ("Can't create LOG_DIR in Func:", export_neglected_file_list)
    try:
        fs.touch(export_path)
        file = fs.open(export_path, 'w')
        for f in backup_file_list:
            try:
                file.write('================================================')
                file.write('\n')
                file.write(fs.filename(f))
                file.write('\n')
                file.write(fs.dirname(f))
                file.write('\n')
            except:
                print("Cant' write export file in func: export_neglected_file_list")
    except:
        print ("cant export in func: export_neglected_file_list")

def main():
    monitoring_dir = get_monitoring_dir(ROOT_DIR, MONITORING_ROOT_DIR)
    # backup_dir_list = get_backup_dir_list(monitoring_dir, ELAPSED_TIME)
    backup_file_list = get_backup_file_list(monitoring_dir, ELAPSED_TIME)
    if len(backup_file_list) > 0:
        export_neglected_file_list(monitoring_dir, ROOT_DIR, LOG_DIR, backup_file_list)
    # if should_create_archive(backup_dir_list):
        # backup_dir_name = get_backup_dir_name(BACKUP_DIR_SUFFIX)
        # create_new_backup_root_dir(ROOT_DIR, TARGET_ROOT_DIR, backup_dir_name)
        # create_archive_tree(monitoring_dir, ROOT_DIR, TARGET_ROOT_DIR, backup_dir_name, backup_dir_list)
    else:
        print ("Nothing to do")

if __name__ == '__main__':
    main()
