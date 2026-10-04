from agents.assistant_agent import Agent
import os


class SystemAgent(Agent):


    def __init__(self):

        super().__init__(
            "System Agent"
        )


    def open_app(self,app):

        print(
        "Opening",
        app
        )


        os.system(
        f"start {app}"
        )