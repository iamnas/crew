class ContractUpdaterTool:
    @staticmethod
    def update_contract(contract_text: str, user_decisions: dict) -> str:
        """Update contract text based on user choices."""
        updated_text = contract_text

        for risk_description, answer in user_decisions.items():
            if answer.lower() == 'y':
                # Very simple logic: Append "Amended based on review" after the line
                updated_text += f"\n\n# Amendment:\nBased on user review, update required: {risk_description}"

        return updated_text
