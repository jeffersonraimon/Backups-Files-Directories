import os
import tarfile
from ftplib import FTP
from datetime import datetime

# ===== CONFIGURATION =====

# Files and/or directories to back up
BACKUP_ITEMS = [
    "/etc/network/interfaces",
    "/etc/keepalived/keepalived.conf",
    "/home/user/scripts"
]

# Temporary directory
BACKUP_DIR = "/tmp"
DATE = datetime.now().strftime("%Y%m%d_%H%M%S")
BACKUP_NAME = "backup_configs_server.tar.gz"
BACKUP_PATH = os.path.join(BACKUP_DIR, BACKUP_NAME)

# FTP settings
FTP_HOST = "ftp.server.lan"
FTP_USER = "backups"
FTP_PASS = "Backups"
FTP_REMOTE_DIR = "/services_configs/server"

# ===== CREATE BACKUP =====

def create_backup():
    print("📦 Creating backup...")
    with tarfile.open(BACKUP_PATH, "w:gz") as tar:
        for item in BACKUP_ITEMS:
            if os.path.exists(item):
                tar.add(item, arcname=item.lstrip("/"))
                print(f"  ✔ Added: {item}")
            else:
                print(f"  ⚠ Not found: {item}")

    print(f"✅ Backup created at: {BACKUP_PATH}")

# ===== SEND VIA FTP =====

def send_ftp():
    print("📤 Sending to FTP...")
    with FTP(FTP_HOST) as ftp:
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd(FTP_REMOTE_DIR)

        with open(BACKUP_PATH, "rb") as f:
            ftp.storbinary(f"STOR {BACKUP_NAME}", f)

    print("✅ Upload completed!")

# ===== CLEANUP =====

def cleanup():
    if os.path.exists(BACKUP_PATH):
        os.remove(BACKUP_PATH)
        print(f"🧹 File removed from /tmp: {BACKUP_PATH}")
    else:
        print("⚠ No file to remove.")

# ===== MAIN =====

if __name__ == "__main__":
    create_backup()
    send_ftp()
    cleanup()
