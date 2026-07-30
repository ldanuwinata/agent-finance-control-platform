import pandas as pd

from src.agents.schema_mapping_agent import SchemaMappingAgent
from src.agents.validation_agent import ValidationAgent
from src.agents.exception_detection_agent import ExceptionDetectionAgent
from src.agents.analysis_agent import AnalysisAgent
from src.agents.report_agent import ReportAgent


def main():

    try:

        print("=" * 50)
        print("Agentic Finance Control Platform")
        print("=" * 50)
        print("Client portfolio onboarding...\n")

        # -------------------------------------------------
        # Step 1 - Load Portfolio
        # -------------------------------------------------

        dataframe = pd.read_csv("data/portfolio.csv")

        # -------------------------------------------------
        # Step 2 - Schema Mapping
        # -------------------------------------------------

        schema_mapper = SchemaMappingAgent()
        mapped_dataframe = schema_mapper.map_schema(dataframe)

        # -------------------------------------------------
        # Step 3 - Validation
        # -------------------------------------------------

        validator = ValidationAgent()

        is_valid, errors = validator.validate(mapped_dataframe)

        if not is_valid:

            print("\n❌ Validation failed\n")

            for error in errors:
                print(f"- {error}")

            return

        print("✅ Validation passed")

        # -------------------------------------------------
        # Step 4 - Exception Detection
        # -------------------------------------------------

        exception_detector = ExceptionDetectionAgent()
        exceptions = exception_detector.detect(mapped_dataframe)

        if exceptions.empty:

            print("\n✅ No portfolio exceptions detected.")

            report_agent = ReportAgent()
            report_agent.export_pdf(
                exceptions,
                [],
                "output/portfolio_exception_report.pdf"
            )

            return

        # -------------------------------------------------
        # Step 5 - AI Analysis
        # -------------------------------------------------

        analysis_agent = AnalysisAgent()
        analyses = analysis_agent.analyse(exceptions)

        # -------------------------------------------------
        # Step 6 - Console Report
        # -------------------------------------------------

        print("\n===== PORTFOLIO REVIEW =====\n")

        for i, (_, row) in enumerate(exceptions.iterrows(), start=1):

            isin = row["ISIN"] if pd.notna(row["ISIN"]) else "N/A"

            print(f"Exception #{i}")
            print("-" * 60)
            print(f"Fund              : {row['Fund']}")
            print(f"ISIN              : {isin}")
            print(f"Number of Shares  : {row['NumberOfShares']}")
            print(f"Market Value      : {row['MarketValue']}")
            print(f"Currency          : {row['Currency']}")
            print(f"Exception         : {row['ExceptionType']}")
            print(f"AI Assessment     : {analyses[i-1]['Analysis']}")
            print()

        # -------------------------------------------------
        # Step 7 - PDF Report
        # -------------------------------------------------

        report_agent = ReportAgent()

        report_agent.export_pdf(
            exceptions,
            analyses,
            "output/portfolio_exception_report.pdf"
        )

        print("\n✅ Pipeline completed successfully.")

    except Exception as e:

        print(f"\n❌ Pipeline failed: {e}")


if __name__ == "__main__":
    main()