from services.llm_service import LLMService
llm = LLMService()

response = llm.ask("What is the capital of France?")

print(response)
