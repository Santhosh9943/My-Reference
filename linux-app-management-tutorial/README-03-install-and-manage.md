# 03 - Installing & Managing Different Package Formats

**Objective:** Install, verify, and remove various package formats with exact commands.

## .deb Packages

```bash
sudo dpkg -i myapp.deb
sudo apt-get install -f         # Fix missing deps
sudo apt-get remove --purge myapp
```

Logs: `/var/log/dpkg.log`

## AppImage

```bash
chmod +x MyApp.AppImage
./MyApp.AppImage
```
To extract & integrate:
```bash
MyApp.AppImage --appimage-extract
sudo mv squashfs-root /opt/myapp
sudo ln -s /opt/myapp/AppRun /usr/local/bin/myapp
```

## tar.gz Archives

```bash
tar xvzf tool.tar.gz -C /opt/tool
cd /opt/tool
sudo mv tool.sh /usr/local/bin/tool
```
Build from source:
```bash
cd /opt/tool/source
./configure --prefix=/usr/local
make && sudo make install
```

## Python (pip3)

```bash
pip3 install tool
pip3 show tool
```

## Node (npm)

```bash
npm install -g tool
npm root -g
```

## Generic Installer Scripts

```bash
sudo ./install.sh --prefix=/opt/mybin
```
