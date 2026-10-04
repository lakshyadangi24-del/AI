from core.logger import logger


class ModelRouter:

    def __init__(self):

        self.models = {

            "general": "llama3.1:8b",

            "coding": "qwen2.5-coder",

            "reasoning": "deepseek-r1",

            "vision": "llava",

            "fast": "phi3"

        }

    def choose_model(self, question):

        text = question.lower()

        coding = [

            "python",
            "java",
            "c++",
            "html",
            "css",
            "javascript",
            "code",
            "program",
            "bug",
            "debug",
            "error",
            "function",
            "class",
            "api"
        ]

        reasoning = [

            "solve",
            "equation",
            "math",
            "physics",
            "chemistry",
            "calculate",
            "proof",
            "logic"
        ]

        vision = [

            "image",
            "photo",
            "picture",
            "camera",
            "recognize",
            "detect"
        ]

        if any(word in text for word in coding):
            logger.info("Router → Coding Model")
            return self.models["coding"]

        if any(word in text for word in reasoning):
            logger.info("Router → Reasoning Model")
            return self.models["reasoning"]

        if any(word in text for word in vision):
            logger.info("Router → Vision Model")
            return self.models["vision"]

        logger.info("Router → General Model")
        return self.models["general"]

    def needs_web(self, question):

        keywords = [

            "today",
            "latest",
            "news",
            "weather",
            "stock",
            "price",
            "current",
            "live",
            "update",
            "recent"

        ]

        question = question.lower()

        return any(word in question for word in keywords)

    def needs_agent(self, text):

        keywords = [
            "create",
            "make",
            "build",
            "open",
            "run",
            "install",
            "code",
            "generate"
        ]

        for word in keywords:

            if word in text.lower():
                return True

        return False