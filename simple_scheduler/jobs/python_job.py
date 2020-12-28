"""A job to run python executable programs."""

from subprocess import call

from ndscheduler.corescheduler import job


class PythonJob(job.JobBase):

    @classmethod
    def meta_info(cls):
        return {
            'job_class_string': '%s.%s' % (cls.__module__, cls.__name__),
            'notes': ('This will run an executable script with a virtual environment interpretor. You can specify as many '
                      'arguments as you want. This job will pass these arguments to the '
                      'program in order.'),
            'arguments': [
                {'type': 'string', 'description': 'Executable path'}
            ],
            'example_arguments': '["/usr/local/my_program", "--file", "/tmp/abc", "--mode", "safe"]'
        }

    def run(self, *args, **kwargs):
        return {'returncode': call(args, **kwargs)}


if __name__ == "__main__":
    # You can easily test this job here
    job = PythonJob.create_test_instance()
    job.run('python', '-m', 'fanqier.helpers')
