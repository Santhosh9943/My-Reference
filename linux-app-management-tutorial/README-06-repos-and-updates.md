# 06 - Local Repositories & Automated Updates

**Objective:** Set up local APT/Flatpak repos and configure auto-updates.

## APT Local Repo

```bash
sudo mkdir -p /srv/debian
cd /srv/debian
sudo dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz
```
Serve via Nginx on `http://localhost/debian/`, then add:
```
deb [trusted=yes] http://localhost/debian ./
```
to `/etc/apt/sources.list.d/local.list`.  
Run:
```bash
sudo apt update
```

## Flatpak Local Repo

```bash
flatpak build-export /srv/flatpak com.example.MyApp
flatpak remote-add --no-gpg-verify local-repo file:///srv/flatpak
flatpak install local-repo com.example.MyApp
```

## Unattended Upgrades

```bash
sudo apt-get install unattended-upgrades apt-listchanges
sudo dpkg-reconfigure unattended-upgrades
```
Ensure `/etc/apt/apt.conf.d/20auto-upgrades` has:
```
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
```

## Snap Auto-Refresh & Rollback

```bash
sudo snap set system refresh.timer=4:00-7:00,19:00-22:10
sudo snap refresh --time
sudo snap revert myapp
```
