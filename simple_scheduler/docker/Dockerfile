FROM python:3.9.1

ARG ssh_prv_key
ARG ssh_pub_key

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub

RUN python3 -m venv /mnt/scheduler && \
    . /mnt/scheduler/bin/activate && \
    pip install -e git+https://github.com/biel-michael/ndscheduler.git#egg=ndscheduler && \
    pip install --no-cache-dir -r /mnt/scheduler/src/ndscheduler/simple_scheduler/requirements.txt 

RUN rm -rf /root/.ssh/

ADD apns.pem /mnt/scheduler/
ADD run_scheduler /mnt/scheduler/bin/run_scheduler
RUN chmod 755 /mnt/scheduler/bin/run_scheduler

CMD ["/mnt/scheduler/bin/run_scheduler"]
