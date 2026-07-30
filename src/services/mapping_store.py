import json
from pathlib import Path


class MappingStore:
    """
    Stores and retrieves learned column mappings.

    Example JSON structure:

    {
        "Invoice Number": {
            "standard_name": "Invoice",
            "source": "llm"
        },
        "Gross Amount": {
            "standard_name": "ActualAmount",
            "source": "llm"
        }
    }
    """

    def __init__(self):
        self.file_path = Path("src/knowledge/column_mappings.json")
        self.mappings = self._load()

    def _load(self):
        """
        Load mappings from the JSON knowledge base.
        """

        if not self.file_path.exists():
            return {}

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def _save(self):
        """
        Save the current mappings to disk.
        """

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                self.mappings,
                file,
                indent=4,
                ensure_ascii=False
            )

    def get_mapping(self, column_name):
        """
        Return the stored mapping for a column.

        Returns:
            dict or None
        """

        return self.mappings.get(column_name)

    def add_mapping(self, column_name, standard_name, source="llm"):
        """
        Store a new mapping and immediately persist it.
        """

        self.mappings[column_name] = {
            "standard_name": standard_name,
            "source": source
        }

        self._save()

    def has_mapping(self, column_name):
        """
        Check whether a mapping already exists.
        """

        return column_name in self.mappings

    def get_standard_name(self, column_name):
        """
        Return only the standardized column name.

        Example:
            "Invoice Number" -> "Invoice"
        """

        mapping = self.get_mapping(column_name)

        if mapping is None:
            return None

        return mapping["standard_name"]

    def remove_mapping(self, column_name):
        """
        Delete a mapping from the knowledge base.
        """

        if column_name in self.mappings:
            del self.mappings[column_name]
            self._save()

    def list_mappings(self):
        """
        Return all learned mappings.
        """

        return self.mappings