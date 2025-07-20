# 🛡️ IntelliJ IDEA Local Backup (Safe & Clean)

[![](https://img.shields.io/badge/IDE-IntelliJ%20IDEA-blue?logo=intellij-idea)](https://www.jetbrains.com/idea/)  
[![](https://img.shields.io/badge/Backup-Type:Settings,Plugins,Recent_Projects-orange)]()  
[![](https://img.shields.io/badge/Safe-✅%20No%20Login/Trial%20Data-green)]()

---

## 📂 What Will Be Backed Up?

- 🔧 IDE Settings (UI, themes, keymaps)
- 🧩 Plugins
- 🧪 Code styles, file templates, inspections
- 🧠 Recently opened projects
- 🚀 Run/Debug configurations

> 🚫 **Excludes**: JetBrains account login, license, trial info

---

## 💾 Backup Paths

### 🪟 Windows
```plaintext
C:\Users\<YourUsername>\.IntelliJIdea<version>\
C:\Users\<YourUsername>\AppData\Roaming\JetBrains\IntelliJIdea<version>\
```

### 🐧 Linux
```bash
~/.config/JetBrains/IntelliJIdea<version>/
```

### 🍏 macOS
```bash
~/Library/Preferences/IntelliJIdea<version>/
```

---

## 🎯 Recommended Folders to Backup

```
<config>/
├── options/              ✅ All IDE settings
├── plugins/              ✅ Installed plugins
├── codestyles/           ✅ Custom code styles
├── templates/            ✅ File templates
├── tasks.xml             ✅ Task and context
└── recentProjects.xml    ✅ Recently opened projects
```

---

## 🛑 Exclude These for Clean Backup
```diff
- eval/                    # License or trial info
- jba_config/              # JetBrains Account config
- *.token / *.key          # Session or auth keys
- user.web.token           # Web token cache
```

---

## 📦 Manual Backup Steps

1. Close IntelliJ IDEA
2. Copy only the safe folders above
3. Zip and store or upload to cloud/local drive

---

## 🔁 Restore Steps

1. Install IntelliJ
2. Paste backed up folders to same path
3. Restart IntelliJ — done!

---

## 🧰 Optional: GUI Method

1. `File → Manage IDE Settings → Export Settings`
2. Select what to include (exclude license)
3. Save `.zip` for portable backup

➡️ Restore via:
```bash
File → Manage IDE Settings → Import Settings
```

---

## 📝 Automated Backup & Restore Script (All Platforms)

### Windows (PowerShell)

**Backup:**
```powershell
$src = "$env:USERPROFILE\.IntelliJIdea<version>"
$dst = "$env:USERPROFILE\Downloads\IntelliJ_Backup.zip"
Compress-Archive -Path $src\* -DestinationPath $dst
```

**Restore:**
```powershell
$src = "$env:USERPROFILE\Downloads\IntelliJ_Backup.zip"
$dst = "$env:USERPROFILE\.IntelliJIdea<version>"
Expand-Archive -Path $src -DestinationPath $dst -Force
```

### macOS/Linux (Bash)

**Backup:**
```bash
SRC="$HOME/.config/JetBrains/IntelliJIdea<version>"
DST="$HOME/Downloads/IntelliJ_Backup.zip"
zip -r "$DST" "$SRC"
```

**Restore:**
```bash
SRC="$HOME/Downloads/IntelliJ_Backup.zip"
DST="$HOME/.config/JetBrains/IntelliJIdea<version>"
unzip -o "$SRC" -d "$DST"
```

> Replace `<version>` with your IntelliJ version (e.g., 2023.2)

---

🧑‍💻 **Author:** Santhosh M  
📘 *Use for local dev backup or setup migration!*
