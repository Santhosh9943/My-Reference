# 📂 Rclone Google Drive CLI Setup Guide

> Author: Santhosh M  
> Last Updated: 2025-07-20

This guide explains how to set up Rclone to connect your Google Drive account using only the command line (CLI). Works on Linux Lite and other Linux distributions.

---

## 🔧 Prerequisites

* ✅ Rclone installed: [https://rclone.org/downloads/](https://rclone.org/downloads/)
* ✅ A Google account
* ✅ Internet access

---

## 📌 Step 1: Launch Rclone config

```bash
rclone config
````

You’ll see:

```
e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q>
```

Choose: `n` → New remote

---

## 📌 Step 2: Name your remote

Example:

```text
name> gdrive_msanthosh9943
```

---

## 📌 Step 3: Choose storage type

It will list many storage types. Type:

```text
13
```

(If Google Drive is option 13. If not, type `drive` and press Enter.)

---

## 📌 Step 4: Client ID and Secret (optional)

* Just press Enter to use the default Rclone client.

  ```
  Google Application Client Id - leave blank  
  Google Application Client Secret - leave blank
  ```

---

## 📌 Step 5: Choose scope

Choose:

```text
1 (Full access - recommended)
```

---

## 📌 Step 6: Configure root folder & advanced settings

* Leave both blank (press Enter)

---

## 📌 Step 7: Auto config (Authorization)

Rclone will ask:

```
Use auto config?
```

* On a desktop with GUI/browser → `Yes`
* On a headless server/SSH → `No`
  → It will give you a URL, open it in your browser, log in, allow access, and paste the verification code back.

---

## 📌 Step 8: Team Drive?

If you're using your personal Google Drive → `No`

---

## ✅ Done!

Rclone will display:

```text
[gdrive_msanthosh9943]
type = drive
scope = drive
token = {"access_token": ...}
```

Now type `q` to quit.

---

## 📂 Step 9: Mount Google Drive

```bash
mkdir -p ~/GoogleDrive
rclone mount gdrive_msanthosh9943: ~/GoogleDrive --vfs-cache-mode full
```

Keep the terminal open while it's mounted.

---

## 🧠 Optional: Run in background

```bash
rclone mount gdrive_msanthosh9943: ~/GoogleDrive --vfs-cache-mode full &
```

---

## 🖥️ Optional: Rclone Web UI

Rclone provides a built-in Web UI for managing remotes and file transfers.

### 👉 Start Rclone Web UI

```bash
rclone rcd --rc-web-gui
```
or
```bash
rclone rcd --rc-web-gui --rc-addr=0.0.0.0:5572 --rc-user=root --rc-pass=root
```

Then visit:

```
http://localhost:5572
```

You can log in with the credentials prompted in the terminal.

> 💡 This Web UI is built and maintained officially by the Rclone team.

---

## 🚀 Auto-mount at boot (Systemd or cron optional)

Let me know if you want a `.service` file to mount it automatically at login.

---

## 🔍 Troubleshooting

| Issue                                 | Fix                                                                                    |             |
| ------------------------------------- | -------------------------------------------------------------------------------------- | ----------- |
| `Transport endpoint is not connected` | Run: `fusermount -uz ~/GoogleDrive`                                                    |             |
| Google Drive quota exceeded           | Wait 24 hours or split file access                                                     |             |
| Rclone not found                      | Reinstall using: \`curl [https://rclone.org/install.sh](https://rclone.org/install.sh) | sudo bash\` |

---

## 🔗 Useful Commands

```bash
rclone lsd gdrive_msanthosh9943:
rclone ls gdrive_msanthosh9943:/
rclone copy somefile.txt gdrive_msanthosh9943:/myfolder/
rclone copy gdrive_msanthosh9943:/myfolder/file.txt ./  # Download to local
rclone move file.txt gdrive_msanthosh9943:/myfolder/     # Move to cloud
rclone sync ./myfolder gdrive_msanthosh9943:/backup/     # Sync local to cloud
rclone delete gdrive_msanthosh9943:/unwantedfile.txt     # Delete remote file
```

---

## 📁 Rclone Configuration Location

Rclone stores its configuration file at:

```bash
~/.config/rclone/rclone.conf
```

You can back this up or move it to another system to reuse the same remote settings.

---

## 📅 List of Rclone Commands

```bash
rclone config               # Open interactive config
rclone copy src: dst:      # Copy files
rclone move src: dst:      # Move files
rclone sync src: dst:      # Sync folders
rclone ls remote:          # List files
rclone lsd remote:         # List directories
rclone mount remote: path  # Mount remote
rclone delete remote:path  # Delete a file or folder
rclone purge remote:path   # Delete all contents
rclone check src: dst:     # Compare files between source and destination
rclone size remote:path    # Get size of folder or files
rclone about remote:       # Info about usage/quota
```

---

## 📌 References

* [Official Rclone Docs](https://rclone.org/drive/)
* [Rclone GitHub](https://github.com/rclone/rclone)

---
