class ContractUpdaterTool:
    @staticmethod
    def process_user_query(user_query: str, contract_text: str) -> (str, str):
        """Chatbot smart updater."""
        reply = ""
        updated_contract = contract_text

        user_query_lower = user_query.lower()

        if "termination" in user_query_lower:
            reply = "✅ Updated termination clause to extend notice to 60 days."
            updated_contract += "\n\nAmendment: Termination notice period extended to 60 days."
        elif "confidentiality" in user_query_lower:
            reply = "✅ Updated confidentiality obligation to 5 years."
            updated_contract += "\n\nAmendment: Confidentiality period now 5 years."
        elif "gdpr" in user_query_lower:
            reply = "✅ Added GDPR compliance clause."
            updated_contract += "\n\nAmendment: GDPR compliance has been added."
        elif "indemnity" in user_query_lower:
            reply = "✅ Added mutual indemnity obligations."
            updated_contract += "\n\nAmendment: Both parties will indemnify each other for breaches."
        else:
            reply = "❓ Sorry, I couldn't understand or match that request to the contract. Try asking about termination, confidentiality, GDPR, or indemnity."

        return reply, updated_contract

# class ContractUpdaterTool:
#     @staticmethod
#     def update_contract(contract_text: str, user_decisions: dict) -> str:
#         """Old batch updating, not used in chatbot."""
#         updated_text = contract_text
#         for risk_description, answer in user_decisions.items():
#             if answer.lower() == 'yes':
#                 updated_text += f"\n\n# Amendment:\n{risk_description}"
#         return updated_text

#     @staticmethod
#     def process_user_query(user_query: str, contract_text: str) -> (str, str):
#         """Chatbot smart updater."""
#         reply = ""
#         updated_contract = contract_text

#         user_query_lower = user_query.lower()

#         if "termination" in user_query_lower:
#             reply = "✅ Updated termination clause to extend notice to 60 days."
#             updated_contract += "\n\nAmendment: Termination notice period extended to 60 days."
#         elif "confidentiality" in user_query_lower:
#             reply = "✅ Updated confidentiality obligation to 5 years."
#             updated_contract += "\n\nAmendment: Confidentiality period now 5 years."
#         elif "gdpr" in user_query_lower:
#             reply = "✅ Added GDPR compliance clause."
#             updated_contract += "\n\nAmendment: GDPR compliance has been added."
#         elif "indemnity" in user_query_lower:
#             reply = "✅ Added mutual indemnity obligations."
#             updated_contract += "\n\nAmendment: Both parties will indemnify each other for breaches."
#         else:
#             reply = "❓ Sorry, I couldn't understand or match that request to the contract. Try asking about termination, confidentiality, GDPR, or indemnity."

#         return reply, updated_contract



# class ContractUpdaterTool:
#     @staticmethod
#     def update_contract(contract_text: str, user_decisions: dict) -> str:
#         """Update contract text based on user choices."""
#         updated_text = contract_text

#         for risk_description, answer in user_decisions.items():
#             if answer.lower() == 'y':
#                 # Very simple logic: Append "Amended based on review" after the line
#                 updated_text += f"\n\n# Amendment:\nBased on user review, update required: {risk_description}"

#         return updated_text
