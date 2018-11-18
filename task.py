class Task():

    def __init__(self, settings={}):

        self._type = "task"
        self._settings = self._validate_settings(settings)

        with open("./soar_scripts/"+self._settings["script"], "r") as f:
            self._code = f.read()

    def _validate_settings(self, settings):

        required = ["id", "name", "script", "entry_point", "imports"]

        for req in required:
            if req not in settings:
                raise ValueError("{} not in task settings".format(req))

        return settings

    def execute(self, data={}):
        for imp in self._settings["imports"]:
            print("importing {}".format(imp))
            globals()[imp] = __import__(imp)

        exec(self._code)
        dummy_func = locals()[self._settings["entry_point"]]
        return dummy_func(data=data, settings=self._settings)
