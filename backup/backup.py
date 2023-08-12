import os
import stat
import shutil
import configparser
import logging
from datetime import datetime


def make_dir_writable(function, path, _):
    """The path on Windows cannot be gracefully removed due to being read-only,
    so we make the directory writable on a failure and retry the original function.
    """
    os.chmod(path, stat.S_IWRITE)
    function(path)


def backup():
    config = configparser.ConfigParser()
    config.read('backup_config.ini')

    logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    max_backups = int(config['Global']['max_backups'])

    for section in config.sections():
        if not section.startswith('Backup_'):
            continue

        source_dir = config[section]['source']
        destination_dir = os.path.join(config[section]['destination'], timestamp)

        # Back up needed directories
        try:
            shutil.copytree(source_dir, destination_dir)
            logging.info(f"Backup of {source_dir} created at {destination_dir}")
        except Exception as e:
            logging.error(f"Error during backup of {source_dir}: {str(e)}")

        # Delete the oldest backups over the limit
        backup_folders = sorted([folder for folder in os.listdir(config[section]['destination']) if
                                 os.path.isdir(os.path.join(config[section]['destination'], folder))])

        if len(backup_folders) > max_backups:
            folders_to_delete = backup_folders[:len(backup_folders) - max_backups]
            for folder in folders_to_delete:
                try:
                    shutil.rmtree(os.path.join(config[section]['destination'], folder), onerror=make_dir_writable)
                    logging.info(f"Deleted old backup: {folder}")
                except Exception as e:
                    logging.error(f"Error during deletion of {source_dir}: {str(e)}")


if __name__ == '__main__':
    backup()
