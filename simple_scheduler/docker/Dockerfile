FROM python:3.9.1

RUN python3 -m venv /mnt/scheduler && \
    . /mnt/scheduler/bin/activate && \
    pip install -e git+https://github.com/biel-michael/ndscheduler.git#egg=ndscheduler && \
    pip install -r /mnt/scheduler/src/ndscheduler/simple_scheduler/requirements.txt

ADD apns.pem /mnt/scheduler/
ADD run_scheduler /mnt/scheduler/bin/run_scheduler
RUN chmod 755 /mnt/scheduler/bin/run_scheduler

CMD ["/mnt/scheduler/bin/run_scheduler"]
