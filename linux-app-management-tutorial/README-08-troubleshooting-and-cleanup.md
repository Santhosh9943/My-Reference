# 08 - Troubleshooting & Cleanup

**Objective:** Use logs and cleanup tools to maintain system health.

## Logs & Fixes

- **dpkg errors**  
  ```bash
  sudo dpkg --configure -a
  sudo apt-get install -f
  tail -f /var/log/dpkg.log
  ```

- **systemd service logs**  
  ```bash
  sudo journalctl -u myapp.service -f
  ```

- **snap logs**  
  ```bash
  sudo snap logs myapp
  ```

- **flatpak repair**  
  ```bash
  flatpak repair
  ```

## GUI Helpers

```bash
sudo apt-get install synaptic gdebi-core appimagelauncher
```
- **Synaptic:** GUI package manager  
- **gdebi:** `gdebi myapp.deb`  
- **AppImageLauncher:** automatic integration

## Cleanup Tools

```bash
sudo apt-get install deborphan
sudo deborphan | xargs sudo apt-get remove --purge
docker system prune -af
flatpak uninstall --unused
sudo snap remove --purge <snap-name>
```
