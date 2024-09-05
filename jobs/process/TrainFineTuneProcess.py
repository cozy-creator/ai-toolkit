from collections import OrderedDict
from ostris_ai_toolkit.jobs import TrainJob
from ostris_ai_toolkit.jobs.process import BaseTrainProcess


class TrainFineTuneProcess(BaseTrainProcess):
    def __init__(self,process_id: int, job: TrainJob, config: OrderedDict):
        super().__init__(process_id, job, config)

    def run(self):
        # implement in child class
        # be sure to call super().run() first
        pass
