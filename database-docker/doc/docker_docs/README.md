# Multi-Database Docker Compose Setup

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
