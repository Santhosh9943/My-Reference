# Multi-Database Docker Setup - Comprehensive Guide

## Table of Contents
1. [Troubleshooting Common Issues](#troubleshooting)
2. [Database Connections](#database-connections)
3. [Admin UI Configuration](#admin-ui-configuration)
4. [Data Management](#data-management)
5. [Performance Optimization](#performance)
6. [Security Best Practices](#security)
7. [Advanced Configuration](#advanced-config)

## <a name="troubleshooting"></a>1. Troubleshooting Common Issues

### Service Startup Failures
**Symptoms**:
- Containers exiting immediately
- "unhealthy" status in `docker compose ps`
- Connection errors in admin UIs

**Diagnosis**:
```bash
docker compose logs -f [service_name]
```

**Common Solutions**:

1. **MongoDB Authentication Issues**:
   ```bash
   MongoServerError: Authentication failed.
   ```
   - Verify credentials in `.env` match for both `mongodb` and `mongo-express` services
   - Reset MongoDB volume:
     ```bash
     docker compose down -v mongodb_data
     docker compose up -d mongodb
     ```

2. **MariaDB Access Denied**:
   ```bash
   Access denied for user 'root'@'localhost' (using password: YES)
   ```
   - Ensure you're using `MARIADB_ROOT_PASSWORD` not `MYSQL_ROOT_PASSWORD`
   - Reset MariaDB volume:
     ```bash
     docker compose down -v mariadb_data
     docker compose up -d mariadb
     ```

3. **Port Conflicts**:
   ```bash
   Error: Port is already allocated
   ```
   - Find conflicting process:
     ```bash
     lsof -i :[PORT]
     ```
   - Change port in `.env` and restart

### Health Check Failures
**Manual Health Checks**:
```bash
# MySQL/MariaDB
docker compose exec mysql mysqladmin ping -u root -p${MYSQL_ROOT_PASSWORD}

# PostgreSQL
docker compose exec postgres pg_isready -U postgres

# MongoDB
docker compose exec mongodb mongosh -u admin -p${MONGO_ROOT_PASSWORD} --eval "db.runCommand({ping:1})"

# Redis
docker compose exec redis redis-cli ping
```

## <a name="database-connections"></a>2. Database Connections

### Connection Strings
**MySQL**:
```
mysql://root:${MYSQL_ROOT_PASSWORD}@localhost:${MYSQL_PORT}/${MYSQL_DATABASE}
```

**MariaDB**:
```
mysql://root:${MARIADB_ROOT_PASSWORD}@localhost:${MARIADB_PORT}/${MARIADB_DATABASE}
```

**PostgreSQL**:
```
postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:${POSTGRES_PORT}/${POSTGRES_DB}
```

**MongoDB**:
```
mongodb://${MONGO_ROOT_USERNAME}:${MONGO_ROOT_PASSWORD}@localhost:${MONGODB_PORT}/?authSource=admin
```

**Redis**:
```
redis://localhost:${REDIS_PORT}
```

### CLI Access
```bash
# MySQL shell
docker compose exec mysql mysql -u root -p${MYSQL_ROOT_PASSWORD}

# PostgreSQL shell
docker compose exec postgres psql -U ${POSTGRES_USER}

# MongoDB shell
docker compose exec mongodb mongosh -u ${MONGO_ROOT_USERNAME} -p${MONGO_ROOT_PASSWORD} --authenticationDatabase admin

# Redis CLI
docker compose exec redis redis-cli
```

## <a name="admin-ui-configuration"></a>3. Admin UI Configuration

### phpMyAdmin
- **Access multiple databases**: Use `PMA_ARBITRARY=1` to connect to any server
- **Connect to MySQL**: Server: `mysql`, Port: `3306`
- **Connect to MariaDB**: Server: `mariadb`, Port: `3306`
- **Troubleshooting**:
  - If databases don't appear, check health of mysql/mariadb services
  - Use root credentials from `.env`

### pgAdmin
1. Login with `${PGADMIN_EMAIL}` and `${PGADMIN_PASSWORD}`
2. Add new server:
   - **Name**: PostgreSQL
   - **Host**: postgres
   - **Port**: 5432
   - **Username**: ${POSTGRES_USER}
   - **Password**: ${POSTGRES_PASSWORD}

### Mongo Express
- **Authentication**: Uses basic auth with `${MONGO_EXPRESS_USERNAME}`/`${MONGO_EXPRESS_PASSWORD}`
- **Connection**: Automatically connects to MongoDB container
- **Troubleshooting**:
  - If connection fails, verify MongoDB health
  - Check `ME_CONFIG_MONGODB_URL` in docker-compose.yml

## <a name="data-management"></a>4. Data Management

### Backup and Restore
**MySQL Backup**:
```bash
docker compose exec -T mysql mysqldump -u root -p${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} > mysql_backup.sql
```

**PostgreSQL Backup**:
```bash
docker compose exec -T postgres pg_dump -U ${POSTGRES_USER} ${POSTGRES_DB} > postgres_backup.sql
```

**MongoDB Backup**:
```bash
docker compose exec -T mongodb mongodump -u ${MONGO_ROOT_USERNAME} -p${MONGO_ROOT_PASSWORD} --authenticationDatabase admin --archive > mongo_backup.archive
```

**Restore MySQL**:
```bash
docker compose exec -T mysql mysql -u root -p${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} < mysql_backup.sql
```

### Volume Management
**List volumes**:
```bash
docker volume ls
```

**Inspect volume**:
```bash
docker volume inspect database-docker_mysql_data
```

**Backup volume**:
```bash
docker run --rm -v database-docker_mysql_data:/volume -v $(pwd):/backup alpine tar cf /backup/mysql_backup.tar /volume
```

## <a name="performance"></a>5. Performance Optimization

### Resource Limits
Add to services in `docker-compose.yml`:
```yaml
deploy:
  resources:
    limits:
      cpus: '0.5'
      memory: 512M
```

### MongoDB Performance
```yaml
mongodb:
  # ...
  command: --wiredTigerCacheSizeGB 1
```

### PostgreSQL Optimization
```yaml
postgres:
  # ...
  environment:
    # ...
    POSTGRES_SHARED_BUFFERS: 256MB
    POSTGRES_EFFECTIVE_CACHE_SIZE: 768MB
```

## <a name="security"></a>6. Security Best Practices

### Critical Security Steps
1. **Change all default passwords** in `.env`
2. **Never commit** `.env` to version control
3. Add to `.gitignore`:
   ```
   .env
   *.bak
   *.tar
   ```

### Production Recommendations
- Use Docker secrets for credentials
- Enable TLS for database connections
- Add network restrictions
- Remove admin UIs in production
- Implement firewall rules
- Use read-only volumes where possible

### Security Scanning
```bash
docker scan mysql
docker scan postgres
docker scan mongo
```

## <a name="advanced-config"></a>7. Advanced Configuration

### Custom Initialization
Add initialization scripts to database services:

**PostgreSQL**:
```yaml
volumes:
  - ./init/postgres:/docker-entrypoint-initdb.d
```

**MongoDB**:
```yaml
volumes:
  - ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js
```

### Network Configuration
Create custom network:
```yaml
networks:
  db-net:
    driver: bridge

services:
  mysql:
    networks:
      - db-net
  # ...
```

### Health Check Customization
Example for MySQL:
```yaml
healthcheck:
  test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-p${MYSQL_ROOT_PASSWORD}"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 30s
```

### Update Strategy
```yaml
deploy:
  update_config:
    parallelism: 1
    delay: 10s
  restart_policy:
    condition: on-failure
    max_attempts: 3
```
````

## File Structure
```
database-docker/
├── docker-compose.yml    # Main compose configuration
├── .env                  # Environment variables (DO NOT COMMIT)
├── sample.env            # Sample environment file
├── README.md             # Main documentation
├── HELP.md               # Detailed help guide
├── init/                 # Custom initialization scripts
│   ├── postgres/
│   │   └── 01-init.sql
│   └── mysql/
│       └── init.sql
└── mongo-init.js         # MongoDB initialization script
```

## Key Features of This Setup
1. **Fixed Authentication**: Resolved MongoDB and MariaDB auth issues
2. **Comprehensive Health Checks**: Ensures dependencies start in correct order
3. **Production-Ready Security**: All credentials externalized, strong defaults
4. **Port Customization**: All ports configurable via environment variables
5. **Detailed Documentation**: Includes troubleshooting, backup procedures, and optimization
6. **Persistent Storage**: Data survives container restarts
7. **Admin UI Integration**: Full suite of database management tools

To use this setup:
1. Save `docker-compose.yml`, `README.md`, and `HELP.md` in a directory
2. Create `.env` from `sample.env`
3. Run `docker compose up -d`
4. Access services at specified ports

The MongoDB and MariaDB authentication issues have been resolved through:
1. Correct environment variable usage
2. Proper health check configuration
3. Authentication database specification
4. Service dependency ordering
5. Volume reset procedures
