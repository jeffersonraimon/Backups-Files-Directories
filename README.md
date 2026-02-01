# Configurations Backup Script

This Python script creates a compressed backup of important configurations files and directories, uploads the backup to an FTP server, and then cleans up the temporary file.

## ✨ Features

- Creates a `.tar.gz` backup archive
- Supports files and directories
- Uploads the backup to a remote FTP server
- Automatically removes the local temporary backup file
- Simple and easy to customize

## 📦 What Gets Backed Up

You can define which files and directories will be included in the backup by editing the `BACKUP_ITEMS` list:

```python
BACKUP_ITEMS = [
    "/etc/network/interfaces",
    "/etc/keepalived/keepalived.conf",
    "/home/user/scripts"
]
```

## ⚙️ Configuration

Edit the following variables to match your environment:

Backup settings

- BACKUP_DIR – Temporary directory (default: /tmp)
- BACKUP_NAME – Name of the backup file

FTP settings

- FTP_HOST – FTP server hostname or IP
- FTP_USER – FTP username
- FTP_PASS – FTP password
- FTP_REMOTE_DIR – Remote directory where the backup will be stored

⚠️ Security tip:
Avoid hardcoding FTP credentials in production environments. Consider using environment variables instead.

## ▶️ How to Run

Make sure you have Python 3 installed, then run:
```bash
python3 backup.py
```
## 🧹 Workflow

Create a compressed backup (.tar.gz)

Upload the backup to the FTP server

Remove the local temporary file

## 📋 Requirements

Python 3.x

FTP access to the destination server

Read permissions for all files and directories being backed up

## 🛠️ Possible Improvements

Use environment variables for credentials

Add logging instead of print

Encrypt the backup file

Add cron support for scheduled backups
