# Multi-Database Docker Environment

![Docker](https://img.shields.io/badge/Docker-100%25%20coverage-blue)
![Databases](https://img.shields.io/badge/Databases-5%20supported-green)

This project provides a complete Docker-based development environment with multiple databases and admin UIs. The setup is ideal for:
- Local development and testing
- Learning different database systems
- Integration testing across multiple database types

## Features

- **Database Services**:
  - MySQL 8
  - MariaDB 10
  - PostgreSQL 16
  - MongoDB 7
  - Redis 7
  
- **Admin UIs**:
  - phpMyAdmin (MySQL/MariaDB)
  - pgAdmin (PostgreSQL)
  - Mongo Express (MongoDB)
  - Redis Commander (Redis)
  - Adminer (Universal)

- **Key Features**:
  - Persistent storage for all databases
  - Health checks for reliable startup
  - Environment variable configuration
  - Automatic restart policies
  - Secure authentication
  - Port customization

## Prerequisites
- Docker Engine (v20.10+)
- Docker Compose (v2.0+)
- 4GB+ RAM recommended

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/database-docker.git
   cd database-docker
   ```

2. **Create environment file**:
   ```bash
   cp sample.env .env
   nano .env  # Edit with your credentials
   ```

3. **Start all services**:
   ```bash
   docker compose up -d
   ```

4. **Verify services are running**:
   ```bash
   docker compose ps
   ```

5. **Access admin interfaces**:
   | Service       | URL                                  | Default Credentials             |
   |---------------|--------------------------------------|---------------------------------|
   | phpMyAdmin    | http://localhost:8080                | root / [MYSQL_ROOT_PASSWORD]    |
   | pgAdmin       | http://localhost:8081                | admin@admin.com / [PGADMIN_PASSWORD] |
   | Mongo Express | http://localhost:8082                | mexpress / [MONGO_EXPRESS_PASSWORD] |
   | Redis Commander| http://localhost:8083               | No authentication               |
   | Adminer       | http://localhost:8084                | Select database and enter credentials |

## Service Configuration

### Database Ports
| Service    | Internal Port | External Port | Environment Variable |
|------------|---------------|---------------|----------------------|
| MySQL      | 3306          | 3306          | MYSQL_PORT           |
| MariaDB    | 3306          | 3307          | MARIADB_PORT         |
| PostgreSQL | 5432          | 5432          | POSTGRES_PORT        |
| MongoDB    | 27017         | 27017         | MONGODB_PORT         |
| Redis      | 6379          | 6379          | REDIS_PORT           |

### Admin UI Ports
| Service       | Internal Port | External Port | Environment Variable |
|---------------|---------------|---------------|----------------------|
| phpMyAdmin    | 80            | 8080          | PHPMYADMIN_PORT      |
| pgAdmin       | 80            | 8081          | PGADMIN_PORT         |
| Mongo Express | 8081          | 8082          | MONGO_EXPRESS_PORT   |
| Redis Commander| 8081          | 8083          | REDIS_COMMANDER_PORT |
| Adminer       | 8080          | 8084          | ADMINER_PORT         |

## Common Commands

```bash
# Start services in background
docker compose up -d

# Stop all services
docker compose down

# View logs for all services
docker compose logs -f

# View logs for specific service
docker compose logs -f mongodb

# Access database shells:
# MySQL
docker compose exec mysql mysql -u root -p

# PostgreSQL
docker compose exec postgres psql -U postgres

# MongoDB
docker compose exec mongodb mongosh -u admin -p

# Rebuild specific service
docker compose up -d --build mongodb

# Remove all data volumes (WARNING: destructive)
docker compose down -v
```

## Customization
Edit the `.env` file to configure:
- Database credentials
- Port mappings
- Admin UI credentials
- Service-specific settings

[View detailed troubleshooting and usage guide](HELP.md)
````
