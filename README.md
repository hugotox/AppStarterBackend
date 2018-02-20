# App Starter Backend

### Run supervisord:

```$ supervisord -c supervisord.conf```

### Reload supervisord:

```$ supervisorctl restart uwsgi```

### Stop supervisord:
```$ supervisorctl stop uwsgi```

### Kill supervisord:
```$ sudo unlink /tmp/supervisor.sock```