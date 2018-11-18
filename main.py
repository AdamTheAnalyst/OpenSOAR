#!/usr/bin/python

from task import Task
from decision import Decision

class PlayBook():


    def start(self):

        task1 = Task(settings={
            "id": "get_url",
            "name": "Get URL",
            "script": "request_file.pysoar",
            "entry_point": "run",
            "imports": ["requests"],
            "url": "https://www.test.com",
        })


        task2 = Task(settings={
            "id": "get_url_bing",
            "name": "Get URL Bing",
            "script": "request_file.pysoar",
            "entry_point": "run",
            "imports": ["requests"],
            "url": "https://www.bing.com",
        })

        dec1 = Decision(settings={
            "id": "bing_or_test",
            "name": "Bing Or Test",
            "condition": "==",
            "left_operand": "query.site",
            "left_operand_dynamic": True,
            "right_operand": "bing",
            "right_operand_dynamic": False,
            "if_false": task1.execute,
            "if_true": task2.execute
        })

        dec1.execute(data={"query.site": "bing"})


if __name__ == "__main__":

    t = PlayBook()
    t.start()

