# 07 - Desktop Shortcut, Launchers & PATH

**Objective:** Integrate apps into desktop environment and shells.

## .desktop File

Create `~/.local/share/applications/myapp.desktop`:

```ini
[Desktop Entry]
Type=Application
Name=MyApp
Comment=Start MyApp
Exec=/usr/local/bin/myapp --profile=prod
Icon=/opt/myapp/icons/myapp.png
Categories=Development;Utility;
Terminal=false
```

Update database:
```bash
update-desktop-database ~/.local/share/applications
```
Add to GNOME Favorites: open Activities, find **MyApp**, right-click ➔ "Add to Favorites".

## Aliases & PATH

Add to `~/.bashrc`:
```bash
echo "alias myapp='/usr/local/bin/myapp'" >> ~/.bashrc
echo 'export PATH="$PATH:/opt/myapp/bin"' >> ~/.bashrc
source ~/.bashrc
```

## Panel/Desktop Launcher

- GNOME: drag from applications overview to Favorites.
- KDE: right-click app ➔ "Add to Panel" or "Add to Desktop".
