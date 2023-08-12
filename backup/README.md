# Server Backup Automation Script Documentation

This document provides instructions for running the Server Backup Automation Script. This script automates the backup process for specified directories on your server.

## Prerequisites

- Python 3.x installed on your server.


## Installation and Configuration

1. Download the `backup.py` and `backup_config.ini` files to a directory on your server.

2. Edit the `backup_config.ini` file to configure your backup settings:
   - In the `[Global]` section, set the maximum number of backups to retain (`max_backups`).
   - For each `[Backup_X]` section, specify the source directory (`source`) and destination backup directory (`destination`).

3. Ensure that you have read and write permissions for the source and destination directories specified in the `backup_config.ini` file.


## Running the Script

1. Open a terminal window.

2. Navigate to the directory containing the script and configuration files using the `cd` command:
   ```shell
   cd /path/to/script/directory
   ```

3. Run the script using the following command:
   ```shell
   python3 backup.py
   ```

The script will create backups of the specified directories and log the process in the backup.log file in the same directory.


## Automating Backups with Cron
You can schedule the script to run automatically at specific intervals using the cron job scheduler.

1. Open your crontab configuration by running:
   ```shell
   crontab -e
   ```

2. Add a new line to the crontab file to schedule the script to run. For example, to run the script every day at 2 AM, add the following line:
   ```shell
   0 2 * * * /usr/bin/python3 /path/to/script/directory/backup.py
   ```

   This line specifies the minute (0), hour (2), and the script's path.


3. Save and exit the crontab editor.


## Monitoring and Troubleshooting
To monitor the script's progress, check the `backup.log` file for logs and any error messages.
Ensure that the script has appropriate permissions to access source and destination directories.
If you encounter any issues, review the script, configuration, and log files for potential problems.
