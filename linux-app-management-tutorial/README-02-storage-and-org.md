# 02 - Default Storage Locations & Organizational Best Practices

**Objective:** Understand default directories and establish a clean organization for manually installed apps.

## Filesystem Hierarchy

- `/usr/bin` – System binaries  
- `/usr/local/bin` – Administrator-installed binaries  
- `/opt` – Optional self-contained packages  
- `~/.local/bin` – Per-user executables  
- `/var/lib/<service>` – Service data/storage  

## Hands‑on: Installing a Sample Tool

1. Create directory:
   ```bash
   sudo mkdir -p /opt/mytool-v1.2.3/bin
   ```
2. Copy binary and symlink:
   ```bash
   sudo cp mytool /opt/mytool-v1.2.3/bin/
   sudo ln -s /opt/mytool-v1.2.3/bin/mytool /usr/local/bin/mytool
   ```
3. Verify:
   ```bash
   which mytool
   echo $PATH
   ```

## Directory Layout Example

```
/opt/apps/
├── mytool-v1.2.3/
│   ├── bin/
│   └── lib/
└── anotherapp/
    ├── bin/
    └── share/
```

## Docker & Kubernetes Volume Mounts

- **Docker:**
  ```bash
  docker run -d -v /opt/apps/mydata:/app/data myimage
  ```
- **Kubernetes Pod Spec:**
  ```yaml
  volumes:
    - name: apps-data
      persistentVolumeClaim:
        claimName: mydata-pvc
  containers:
    - name: myapp
      image: myimage
      volumeMounts:
        - name: apps-data
          mountPath: /opt/apps/mydata
  ```
