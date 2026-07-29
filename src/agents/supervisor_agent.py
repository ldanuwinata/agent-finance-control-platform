from agents.validation_agent import ValidationAgent
from agents.analysis_agent import AnalysisAgent
from agents.evidence_agent import EvidenceAgent
from agents.report_agent import ReportAgent
from models.workflow_result import WorkflowResult

class SupervisorAgent:
    
    def __init__(self):
        self.validation_agent = ValidationAgent()
        self.analysis_agent = AnalysisAgent()
        self.evidence_agent = EvidenceAgent()
        self.report_agent = ReportAgent()

    def process(self, dataframe) -> WorkflowResult:
        
        validated = self.validation_agent.validate(dataframe)
        exceptions = self.validation_agent.get_exceptions(validated)
        analyses = self.analysis_agent.analyse(exceptions)
        evidence = self.evidence_agent.collect(exceptions)
        report = self.report_agent.generate({
            "validated": validated,
            "exceptions": exceptions,
            "analysis": analyses,
            "evidence": evidence,
        })

        return WorkflowResult(
            validated=validated,
            exceptions=exceptions,
            analysis=analyses,
            evidence=evidence,
            report=report
        )


