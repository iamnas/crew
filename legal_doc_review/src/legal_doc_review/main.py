# # #!/usr/bin/env python
# # import warnings
# # from datetime import datetime

# # from crew import LegalDocReview

# # warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# # def run():
# #     """
# #     Run the Legal Document Review crew.
# #     """
# #     inputs = {
# #         'legal_document': """
# #         THIS AGREEMENT made as of April 10, 2025, between Alpha Corporation and Beta LLC.
# #         WHEREAS, the parties wish to enter into a confidential agreement regarding project deliverables.
# #         Termination rights shall exist with 30 days' notice.
# #         (Insert more detailed legal document text here)
# #         """
# #     }
# #     try:
# #         LegalDocReview().crew().kickoff(inputs=inputs)
# #     except Exception as e:
# #         raise Exception(f"An error occurred while running the crew: {e}")


# # if __name__ == "__main__":
# #     run()

# #!/usr/bin/env python
# import os
# import warnings

# from crew import LegalDocReview
# from tools.document_loader_tool import DocumentLoaderTool

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# def run():
#     """
#     Run the Legal Document Review crew.
#     """
#     # Load the legal document from file
#     document_loader = DocumentLoaderTool()
#     legal_document = document_loader._run('samples/legal_document.txt')

#     inputs = {
#         'legal_document': legal_document
#     }
    
#     try:
#         result = LegalDocReview().crew().kickoff(inputs=inputs)

#         # Save the results
#         os.makedirs('outputs', exist_ok=True)

#         if isinstance(result, str):
#             with open('outputs/final_report.txt', 'w', encoding='utf-8') as f:
#                 f.write(result)
#             print("✅ Final report saved to outputs/final_report.txt")
#         else:
#             print("Unexpected result format (expected string). Got:", type(result))
            
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")

#         # if isinstance(result, dict):
#         #     with open('outputs/clauses_output.txt', 'w', encoding='utf-8') as f:
#         #         f.write(result.get('extract_clauses_task', 'No clause extraction result'))

#         #     with open('outputs/risk_report.txt', 'w', encoding='utf-8') as f:
#         #         f.write(result.get('detect_risks_task', 'No risk detection result'))

#         #     with open('outputs/summary_output.txt', 'w', encoding='utf-8') as f:
#         #         f.write(result.get('summarize_document_task', 'No summary result'))
#         # else:
#         #     print("Unexpected result format:", result)
#     # except Exception as e:
#     #     raise Exception(f"An error occurred while running the crew: {e}")

# if __name__ == "__main__":
#     run()



#!/usr/bin/env python
import os
import warnings

from crew import LegalDocReview
from tools.document_loader_tool import DocumentLoaderTool

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the Legal Document Review crew.
    """
    # Load the legal document from file
    document_loader = DocumentLoaderTool()
    # legal_document = document_loader._run(file_path='samples/legal_document.txt')
    file_path = os.path.join(os.path.dirname(__file__), 'samples', 'legal_document.txt')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    legal_document = document_loader._run(file_path=file_path)
    if not legal_document:
        raise ValueError("Failed to load the legal document. Please check the file path and content.")
    # Check if the document is empty
    if not legal_document.strip():
        raise ValueError("The legal document is empty. Please provide a valid document.")
    # Prepare inputs for the crew
    print("Loaded legal document successfully.", legal_document[:100], "...")  # Print the first 100 characters for verification

    inputs = {
        'legal_document': legal_document
    }
    
    try:
        result = LegalDocReview().crew().kickoff(inputs=inputs)

        # Save results
        os.makedirs('outputs', exist_ok=True)

        # Check if the result is a CrewOutput object
        print("Result type:", type(result),result)  # Debugging line
        
        # Now result is a CrewOutput object
        # final_text = result.final_output

        # with open('outputs/final_report.txt', 'w', encoding='utf-8') as f:
        #     f.write(final_text)

        print("✅ Final report saved to outputs/final_report.txt")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()



