from dataclasses import dataclass
import pandas as pd

@dataclass
class WorkflowResult:
    validated: pd.DataFrame
    exceptions: pd.DataFrame
    analysis: list
    evidence: list
    report: str
    