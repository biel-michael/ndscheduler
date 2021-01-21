# Dockerize simple scheduler

## Build docker image
```bash
docker build --no-cache -t ndscheduler --build-arg ssh_prv_key="$(cat ~/.ssh/id_ed25519)" --build-arg ssh_pub_key="$(cat ~/.ssh/id_ed25519.pub)" --build-arg ssh_jira_automaton_prv_key="$(cat ~/.ssh/id_ed25519_jira_automaton)" --build-arg ssh_jira_automaton_pub_key="$(cat ~/.ssh/id_ed25519_jira_automaton.pub)" --build-arg ssh_conf="$(cat ~/.ssh/config)" .
```

## Run a container

```bash
    docker run -it -p 8888:8888 --env-file=.env --mount type=bind,source=$ABS_PATH_TO_DATASTORE,target=/datastore.db --name=ndscheduler ndscheduler
```

You can now access the localhost:8888 for the web UI. The job store would be persisted over various docker start run using the host's datastore copy.
