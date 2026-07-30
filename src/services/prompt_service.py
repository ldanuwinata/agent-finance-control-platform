from pathlib import Path


class PromptService:

    def __init__(self):
        self.prompt_folder = Path("src/prompts")

    def load_prompt(self, filename: str, **kwargs) -> str:
        path = self.prompt_folder / filename

        if not path.exists():
            raise FileNotFoundError(f"Prompt '{filename}' not found.")

        template = path.read_text(encoding="utf-8")

        try:
            return template.format(**kwargs)
        except KeyError as e:
            raise ValueError(
                f"Missing placeholder value for '{e.args[0]}' in prompt '{filename}'."
            )