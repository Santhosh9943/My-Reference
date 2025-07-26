# 01 - Inventory & Audit of Installed Applications

**Objective:** Produce a consolidated inventory report of all installed applications and services.

## Commands to List Installed Components

- **Debian packages**  
  ```bash
  dpkg -l | grep '^ii'
  ```
  Lists all installed `.deb` packages.

- **Snap packages**  
  ```bash
  snap list
  ```

- **Flatpak apps**  
  ```bash
  flatpak list --app
  ```

- **AppImages and tarballs**  
  ```bash
  ls ~/Downloads/*.AppImage 2>/dev/null
  ls ~/Downloads/*.{tar.gz,tgz} 2>/dev/null
  ```

- **Python packages (pip3)**  
  ```bash
  pip3 list
  ```

- **Node packages (npm)**  
  ```bash
  npm list -g --depth=0
  ```

- **Docker images & containers**  
  ```bash
  docker images
  docker ps -a
  ```

- **Kubernetes workloads**  
  ```bash
  kubectl get deployments,pods --all-namespaces
  ```

## Audit Script

Create a Bash script to gather all info into `~/app-inventory.txt`:

```bash
cat << 'EOF' > ~/audit-apps.sh
#!/bin/bash
{
  echo "=== dpkg packages ==="
  dpkg -l | grep '^ii'
  echo "=== Snap packages ==="
  snap list
  echo "=== Flatpak packages ==="
  flatpak list --app
  echo "=== AppImages in Downloads ==="
  ls ~/Downloads/*.AppImage 2>/dev/null
  echo "=== Tarballs in Downloads ==="
  ls ~/Downloads/*.{tar.gz,tgz} 2>/dev/null
  echo "=== pip packages ==="
  pip3 list
  echo "=== npm packages ==="
  npm list -g --depth=0
  echo "=== Docker images ==="
  docker images
  echo "=== Docker containers ==="
  docker ps -a
  echo "=== Kubernetes deployments & pods ==="
  kubectl get deployments,pods --all-namespaces
} > ~/app-inventory.txt
EOF

chmod +x ~/audit-apps.sh
echo "Run ./audit-apps.sh to generate ~/app-inventory.txt"
```
