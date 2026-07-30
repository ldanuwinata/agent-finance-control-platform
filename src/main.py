import pandas as pd

from logger import get_logger
from agents.supervisor_agent import SupervisorAgent
from config import DATA_PATH, REPORT_PATH

logger = get_logger(__name__)

def main():
    logger.info("Starting Agentic Finance Control Platform")

    # Load the transactions data
    df = pd.read_csv('data/transactions.csv')
    print(df.columns)
    
    logger.info(f"Loaded {len(df)} transactions.csv.")

    # Run the workflow
    supervisor_agent = SupervisorAgent()
    results = supervisor_agent.process(df)

    logger.info("Workflow completed.")

    # Print the generated report
    print(results.report)

    # Save the report
    with open('data/report.txt', 'w') as f:
        f.write(results.report)

    logger.info("Report saved to data/report.txt.")

    results = supervisor_agent.process(df)
    print(type(results))

if __name__ == "__main__":
    main()


