class EvidenceAgent:

    def collect(self, exceptions):

        evidence = []

        for _, row in exceptions.iterrows():

            invoice = row['Invoice']

            evidence.append({
                "Invoice": invoice,
                "Supporting Documents": f"Supporting documents for invoice {invoice}.pdf",
                "Status": "Found"
            })

        return evidence
