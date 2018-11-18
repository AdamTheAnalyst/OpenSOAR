id: 40202fbb-9ed4-4b8f-86e1-68722d808e3d
version: 0
name: Example-Playbook
description: This playbook is an example hello world
starttaskid: "0"
tasks:
  "0":
    id: "0"
    taskid: c44160b9-16d8-4a1e-8765-1c034006a184
    type: task
    task:
      id: "get_isbn"
      name: "Lookup ISBN"
      script: "request_json.pysoar"
      entry_point: "run"
      url: "https://www.booknomads.com/api/v0/isbn/"
      imports: 
        - "requests"
        - "json"
    nextstep: "1"
  "1":
    id: "1"
    taskid: c44160b9-16d8-4a1e-8765-1c034006a186
    type: condition
    task:
      id: "c44160b9-16d8-4a1e-8765-1c034006a186"
      name: "If book is Dutch"
      condition: "=="
      left_operand: "nl"
      right_operand: "get_isbn.response"
      left_operand_dynamic: False
      right_operand_dynamic: True
      if_false: "2"
      if_true: "3"
  "2":
    id: "2"
    taskid: c44160b9-16d8-4a1e-8765-1c034006a188
    type: task
    task:
      id: c44160b9-16d8-4a1e-8765-1c034006a188
      name: "Not A Dutch Book"
      script: "test_print.pysoar"
      entry_point: "run"
      imports: []
    nextstep: False
  "3":
    id: "3"
    taskid: c44160b9-16d8-4a1e-8765-1c034006a181
    type: task
    task:
      id: c44160b9-16d8-4a1e-8765-1c034006a181
      name: "A Dutch Book!"
      script: "test_print.pysoar"
      entry_point: "run"
      imports: []
    nextstep: False