import ollama

from agents.manager import AgentManager

from core.router import ModelRouter

from memory.database import MemoryDatabase

from core.logger import logger

from core.web_search import WebSearch


class LaxisBrain:

    def __init__(self):

        self.memory = MemoryDatabase()

        self.router = ModelRouter()

        self.web = WebSearch()

        self.agents = AgentManager()

        logger.info("Brain Online")

    def ask(self, question):

        # Agent Check
        if self.router.needs_agent(question):
            result = self.agents.execute(question)

            return result

        # Get previous conversation
        history = self.memory.get_history()

        messages = []

        for user, ai in history:
            messages.append({
                "role": "user",
                "content": user
            })

            messages.append({
                "role": "assistant",
                "content": ai
            })

        # ---------- Internet Search ----------
        if self.router.needs_web(question):

            results = self.web.search(question)

            context = ""

            for item in results:
                context += f"""
    Title: {item['title']}

    Summary: {item['body']}

    """

            question = f"""
    Use the following web information to answer accurately.

    {context}

    User Question:
    {question}
    """

        # Add final question
        messages.append({
            "role": "user",
            "content": question
        })

        # Select AI model
        model = self.router.choose_model(question)

        # Ask Ollama
        response = ollama.chat(
            model=model,
            messages=messages
        )

        answer = response["message"]["content"]

        # Save conversation
        self.memory.save(question, answer)

        return answer