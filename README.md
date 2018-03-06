# App Starter Backend

### Run supervisord:

```$ supervisord -c supervisor-app.conf```

### Reload supervisord:

```$ supervisorctl restart uwsgi```

### Stop supervisord:
```$ supervisorctl stop uwsgi```

### Kill supervisord:
```$ sudo unlink /tmp/supervisor.sock```

## Run with Docker

```$ docker build -t backend .```

```$ docker run -d -p 80:80 backend```