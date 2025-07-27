# Docker Compose Cheat Sheet

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
