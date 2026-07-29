class ReportAgent:
    def generate(self, results):

        report = []

        report.append("\n===== REPORT =====\n")

        report.append(
            f"Transactions checked : {len(results['validated'])}"
        )

        report.append(
            f"Exceptions found : {len(results['exceptions'])}\n"
        )

        report.append("Exception Details:\n")

        for analysis in results["analysis"]:
            report.append(f"- {analysis}")

        report.append("\nSupporting Evidence:\n")

        for evidence in results["evidence"]:
            report.append(
                f"- Invoice {evidence['Invoice']} : "
                f"{evidence['Supporting Documents']}"
            )

        return "\n".join(report)
