#!/usr/bin/python

import yaml
import sys

from task import Task
from decision import Decision


class PlayBook():

    def __init__(self, playbook_path):

        with open(playbook_path, "r") as f:
            self._pb = yaml.load(f.read())

        self._step = self._pb["starttaskid"]
        self._tasks = {}

        for task_id in self._pb["tasks"]:

            task_settings = self._pb["tasks"][task_id]["task"]
            if self._pb["tasks"][task_id]["type"] == "task":
                self._tasks[task_id] = Task(settings=task_settings)

            elif self._pb["tasks"][task_id]["type"] == "condition":
                self._tasks[task_id] = Decision(settings=task_settings)

    def start(self, data={}):

        c_step = self._step

        while c_step:
            active = self._tasks[c_step]

            if active._type == "task":
                data = active.execute(data=data)
                c_step = self._pb["tasks"][c_step]["nextstep"]

            elif active._type == "condition":
                result = active.execute(data=data)
                if result:
                    c_step = self._pb["tasks"][c_step]["task"]["if_true"]
                else:
                    c_step = self._pb["tasks"][c_step]["task"]["if_false"]


if __name__ == "__main__":

    t = PlayBook(sys.argv[1])
    t.start(data={"isbn": "9789000035526"})
