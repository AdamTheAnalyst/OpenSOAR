class Decision():

    def __init__(self, settings={}):

        self._settings = self._validate_settings(settings)

        self._id = settings["id"]
        self._name = settings["name"]
        self._condition = settings["condition"]
        self._left_operand = settings["left_operand"]
        self._left_operand_dynamic = settings["left_operand_dynamic"]
        self._right_operand = settings["right_operand"]
        self._right_operand_dynamic = settings["right_operand_dynamic"]
        self._exec_if_true = settings["if_false"]
        self._exec_if_false = settings["if_true"]

    def _validate_settings(self, settings):

        required = ["condition", "left_operand", "right_operand",
                    "left_operand_dynamic", "right_operand_dynamic",
                    "if_false", "if_true", "id", "name"]

        for req in required:
            if req not in settings:
                raise ValueError("{} not in decision settings".format(req))

        return settings


    def execute(self, data={}):

        # Left Operand
        if self._left_operand_dynamic:
            if isinstance(data[self._left_operand], int):
                left = data[self._left_operand]
            else:
                left = "'{}'".format(data[self._left_operand])
        else:
            if isinstance(self._left_operand, int):
                left = self._left_operand
            else:
                left = "'{}'".format(self._left_operand)

        # Right Operand
        if self._right_operand_dynamic:
            if isinstance(data[self._right_operand], int):
                right = data[self._right_operand]
            else:
                right = "'{}'".format(data[self._right_operand])
        else:
            if isinstance(self._right_operand, int):
                right = self._right_operand
            else:
                right = "'{}'".format(self._right_operand)

        # Run comparison
        if eval("{} {} {}".format(left, self._condition, right)):
            self._exec_if_true(data=data)
        else:
            self._exec_if_false(data=data)