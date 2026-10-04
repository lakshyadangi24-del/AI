from agents.planner import PlannerAgent
from agents.coding_agent import CodingAgent
from agents.system_agent import SystemAgent



class AgentManager:


    def __init__(self):

        self.planner = PlannerAgent()

        self.coder = CodingAgent()

        self.system = SystemAgent()



    def execute(self, task):


        plan = self.planner.create_plan(task)


        print("\nPLAN:")

        for step in plan:
            print("-", step)



        task = task.lower()



        # Coding Agent
        coding_words = [
            "code",
            "program",
            "software",
            "app",
            "script",
            "create"
        ]


        for word in coding_words:

            if word in task:

                return self.coder.write_code(task)



        # System Agent
        system_words = [
            "open",
            "launch",
            "start",
            "run"
        ]


        for word in system_words:

            if word in task:

                return self.system.open_app(task)



        return "No suitable agent found"