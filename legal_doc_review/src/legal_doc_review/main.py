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

    # inputs = {
    #     'legal_document': legal_document
    # }
    file_path = os.path.join(os.path.dirname(__file__), 'samples', 'confidentiality_agreement.txt')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    legal_document = document_loader._run(file_path=file_path)
    if not legal_document:
        raise ValueError("Failed to load the legal document. Please check the file path and content.")
    # Check if the document is empty
    if not legal_document.strip():
        raise ValueError("The legal document is empty. Please provide a valid document.")
    # Prepare inputs for the crew
    # print("Loaded legal document successfully.", legal_document[:100], "...")  # Print the first 100 characters for verification

    inputs = {
        'legal_document': legal_document
    }
    
    
    try:
        LegalDocReview().crew().kickoff(inputs=inputs)
        print("✅ Crew finished. Output file generated automatically!")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()

