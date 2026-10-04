class Agent:

    def __init__(self,name):
        self.name = name


    def run(self,task):

        print(
            f"{self.name} working on {task}"
        )

        return "Task completed"