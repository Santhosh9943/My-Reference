import os
import zipfile

# Markdown file contents
files_content = {
    "CHEAT_SHEET.md": """# Docker Compose Cheat Sheet

## Start All Services
```bash
docker-compose up -d
```

## Stop All Services
```bash
docker-compose down
```

## Check Logs for a Service
```bash
docker-compose logs <service_name>
```

## Restart a Service
```bash
docker-compose restart <service_name>
```

## Access MySQL CLI
```bash
docker exec -it <mysql_container> mysql -u root -p
```

## Access PostgreSQL CLI
```bash
docker exec -it <postgres_container> psql -U admin -d app_db
```

## Access MongoDB Shell
```bash
docker exec -it <mongodb_container> mongosh -u admin -p admin
```

## Access Redis CLI
```bash
docker exec -it <redis_container> redis-cli
```
""",
    "README.md": """# Multi-Database Docker Compose Setup

This setup runs MySQL, MariaDB, PostgreSQL, MongoDB, Redis with UI tools like phpMyAdmin, pgAdmin, Mongo Express, Redis Commander, and Adminer.

## 📦 Services Included
- MySQL + phpMyAdmin
- MariaDB + phpMyAdmin
- PostgreSQL + pgAdmin
- MongoDB + Mongo Express
- Redis + Redis Commander
- Adminer (for universal DB access)

## 🚀 Usage
1. Copy `.env.example` to `.env` and update values if needed.
2. Start the services:
```bash
docker-compose up -d
```
3. Stop services:
```bash
docker-compose down
```

## 🔑 Default Credentials
- **MySQL/MariaDB**: root/root
- **PostgreSQL**: admin/admin
- **MongoDB**: admin/admin
- **Redis**: No password (default)
- **pgAdmin**: admin@admin.com / admin
- **Mongo Express**: admin/admin
""",
    "HELP.md": """# Help - Docker Compose Database Stack

## Environment Variables
You can override ports and credentials via `.env` file:

```
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=app_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
MONGO_ROOT_USERNAME=admin
MONGO_ROOT_PASSWORD=admin
REDIS_PORT=6379
```

## Healthchecks
Each database has a healthcheck to ensure the container is ready before dependent services start.

## Networks and Volumes
- Uses `backend` network.
- Persistent volumes for all databases.

## Common Issues
- **Port conflicts:** Change ports in `.env`.
- **Volume permissions:** Run `sudo chown -R $USER:$USER ./`.
- **Restart stack:** `docker-compose down -v && docker-compose up -d`.
"""
}

# Create output directory
output_dir = "docker_docs"
os.makedirs(output_dir, exist_ok=True)

# Write markdown files
for filename, content in files_content.items():
    with open(os.path.join(output_dir, filename), "w") as f:
        f.write(content)

# Create ZIP file
zip_filename = "docker_docs_bundle.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for filename in files_content.keys():
        zipf.write(os.path.join(output_dir, filename), filename)

print(f"✅ ZIP file created: {zip_filename}")
