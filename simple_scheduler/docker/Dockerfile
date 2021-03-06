FROM python:3.9.1

ARG ssh_prv_key
ARG ssh_pub_key
ARG ssh_jira_automaton_prv_key
ARG ssh_jira_automaton_pub_key
ARG ssh_conf

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_ed25519 && \
    echo "$ssh_pub_key" > /root/.ssh/id_ed25519.pub && \
    echo "$ssh_jira_automaton_prv_key" > /root/.ssh/id_ed25519_jira_automaton && \
    echo "$ssh_jira_automaton_pub_key" > /root/.ssh/id_ed25519_jira_automaton.pub && \
    echo "$ssh_conf" > /root/.ssh/config && \
    chmod 600 /root/.ssh/id_ed25519 && \
    chmod 600 /root/.ssh/id_ed25519.pub && \
    chmod 600 /root/.ssh/id_ed25519_jira_automaton && \
    chmod 600 /root/.ssh/id_ed25519_jira_automaton.pub && \
    chmod 600 /root/.ssh/config

RUN python3 -m venv /mnt/scheduler && \
    . /mnt/scheduler/bin/activate && \
    pip install -e git+https://github.com/biel-michael/ndscheduler.git#egg=ndscheduler

RUN . /mnt/scheduler/bin/activate && \
    pip install -e git+ssh://git@github.com-jira-automaton/BIEL-Datalab/jira-automaton.git#egg=jira-automaton
RUN . /mnt/scheduler/bin/activate && \
    pip install -e git+ssh://git@github.com-fastapi/BIEL-Datalab/fastapi.git#egg=biel-fastapi
RUN . /mnt/scheduler/bin/activate && \
    pip install --no-cache-dir -r /mnt/scheduler/src/ndscheduler/simple_scheduler/requirements.txt

RUN rm -rf /root/.ssh/

ADD run_scheduler /mnt/scheduler/bin/run_scheduler
RUN chmod 755 /mnt/scheduler/bin/run_scheduler

EXPOSE 8888

CMD ["/mnt/scheduler/bin/run_scheduler"]