import os
import subprocess


class AppControl:

    def open_app(self, name: str):

        name = name.lower()

        apps = {
            "chrome": "start chrome",
            "edge": "start msedge",
            "notepad": "notepad",
            "calculator": "calc",
            "paint": "mspaint",
            "cmd": "cmd",
            "explorer": "explorer"
        }

        if name in apps:
            os.system(apps[name])
            return f"{name} opened."

        return "Application not found."