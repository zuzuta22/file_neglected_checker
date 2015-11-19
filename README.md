# README

# Description
This scripts is designed to export a file list which consists of files which has not been accessed for some certain period.
In future, not just exporting log but also create backup automatically.

# Usage
`python file_neglected_checker`

The following variable should be changed for your need

- ROOT_DIR = fs.home()
- MONITORING_ROOT_DIR = 'Dropbox/'
- TARGET_ROOT_DIR = 'Dropbox/_Archives'
- LOG_DIR = 'Dropbox/_Archives/Log'
- BACKUP_DIR_SUFFIX = '_archives'
- ELAPSED_TIME = 7776000  #7776000 seconds = 90 days

## Condition
This script has been tested only under Python 3.4.3
