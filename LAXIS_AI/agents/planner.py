from agents.assistant_agent import Agent


class PlannerAgent(Agent):

    def __init__(self):
        super().__init__("Planner Agent")


    def create_plan(self,task):

        print(
        "\nCreating plan..."
        )


        plan=[]


        if "code" in task.lower():

            plan=[
                "Research requirements",
                "Write code",
                "Test program"
            ]


        else:

            plan=[
                "Understand task",
                "Find solution",
                "Execute"
            ]


        return plan