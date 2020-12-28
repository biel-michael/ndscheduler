"""Run the scheduler process."""

from ndscheduler.server import server


class SimpleServer(server.SchedulerServer):

    def post_scheduler_start(self):
        jobs = self.scheduler_manager.get_jobs()
        return jobs


if __name__ == "__main__":
    SimpleServer.run()
