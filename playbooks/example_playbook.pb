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
      id: "get_url"
      name: "Request A File"
      script: "request_file.pysoar"
      entry_point: "run"
      url: "http://www.bing.com"
      imports: 
        - "requests"
    nextstep: "1"
  "1":
    id: "1"
    taskid: c44160b9-16d8-4a1e-8765-1c034006a186
    type: condition
    task:
      id: "c44160b9-16d8-4a1e-8765-1c034006a186"
      name: "If URL contains bing"
      condition: "=="
      left_operand: 201
      right_operand: "get_url.status_code"
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
      name: "Printy 1"
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
      name: "Printy 2"
      script: "test_print.pysoar"
      entry_point: "run"
      imports: []
    nextstep: False