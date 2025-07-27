# Help - Docker Compose Database Stack

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
