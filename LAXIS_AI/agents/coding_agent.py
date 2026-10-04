from agents.assistant_agent import Agent


class CodingAgent(Agent):


    def __init__(self):

        super().__init__(
            "Coding Agent"
        )


    def write_code(self,task):

        print(
        "Writing code for:",
        task
        )


        return "Code generated"