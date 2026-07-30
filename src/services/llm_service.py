from ollama import chat


class LLMService:
    """
    Service responsible for communicating with the local LLM.
    """

    def __init__(self, model: str = "qwen3:4b"):
        self.model = model

    def ask(self, prompt: str) -> str:
        try:
            response = chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.message.content

        except Exception as e:
            return f"LLM Error: {e}"
