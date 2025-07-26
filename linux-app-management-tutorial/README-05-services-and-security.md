# 05 - Update‑Alternatives, SELinux/AppArmor & systemd

**Objective:** Manage versions, security contexts, and integrate services.

## Update-Alternatives (Java Example)

```bash
sudo update-alternatives --install /usr/bin/java java /opt/java-8/bin/java 1080
sudo update-alternatives --install /usr/bin/java java /opt/java-11/bin/java 1100
sudo update-alternatives --config java
update-alternatives --display java
```

## SELinux Contexts

```bash
sudo chcon -R -t bin_t /opt/apps/myapp
# To persist:
sudo semanage fcontext -a -t bin_t "/opt/apps/myapp(/.*)?"
sudo restorecon -R /opt/apps/myapp
```

## AppArmor Profile

Create `/etc/apparmor.d/myapp`:
```
/opt/myapp/bin/myapp {
  #include <abstractions/base>
  /opt/myapp/bin/myapp Px,
  /opt/myapp/lib/** mr,
  /etc/ld.so.cache r,
  /usr/lib/** r,
}
```
Load profile:
```bash
sudo apparmor_parser -r /etc/apparmor.d/myapp
```

## systemd Service

Place `myapp.service` in `/etc/systemd/system/`:

```ini
[Unit]
Description=My App Service
After=network.target

[Service]
ExecStart=/opt/myapp/bin/start.sh
Restart=on-failure
Environment=APP_ENV=production

[Install]
WantedBy=multi-user.target
```

Enable & start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp.service
sudo systemctl start myapp.service
```
User service (`~/.config/systemd/user/`): use `systemctl --user`.
