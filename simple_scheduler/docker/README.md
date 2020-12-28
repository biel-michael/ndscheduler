# Dockerize simple scheduler

## Build docker image
```bash
  docker build -t ndscheduler --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" --build-arg ssh_pub_key="$(cat ~/.ssh/id_rsa.pub)" .
```

## Run a container

```bash
    docker run -it -p 8888:8888 --env-file=.env --mount type=bind,source=$ABS_PATH_TO_DATASTORE,target=/datastore.db --name=ndscheduler ndscheduler
```

You can now access the localhost:8888 for the web UI. The job store would be persisted over various docker start run using the host's datastore copy.
