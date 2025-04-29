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
#     # legal_document = document_loader._run(file_path='samples/legal_document.txt')

#     # inputs = {
#     #     'legal_document': legal_document
#     # }
#     file_path = os.path.join(os.path.dirname(__file__), 'samples', 'confidentiality_agreement.txt')

#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"File not found: {file_path}")
#     legal_document = document_loader._run(file_path=file_path)
#     if not legal_document:
#         raise ValueError("Failed to load the legal document. Please check the file path and content.")
#     # Check if the document is empty
#     if not legal_document.strip():
#         raise ValueError("The legal document is empty. Please provide a valid document.")
#     # Prepare inputs for the crew
#     # print("Loaded legal document successfully.", legal_document[:100], "...")  # Print the first 100 characters for verification

#     inputs = {
#         'legal_document': legal_document
#     }
    
    
#     try:
#         LegalDocReview().crew().kickoff(inputs=inputs)
#         print("✅ Crew finished. Output file generated automatically!")
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")

# if __name__ == "__main__":
#     run()




# #!/usr/bin/env python
# import os
# import warnings

# from tools.document_loader_tool import DocumentLoaderTool
# from tools.document_chunker_tool import DocumentChunkerTool
# from tools.contract_updater_tool import ContractUpdaterTool
# from processors.chunk_processor import ChunkProcessor
# from processors.result_merger import ResultMerger
# from processors.question_processor import QuestionProcessor

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# def run():
#     loader = DocumentLoaderTool()
#     chunker = DocumentChunkerTool()

#     file_path = os.path.join(os.path.dirname(__file__), 'samples', 'confidentiality_agreement.txt')
#     contract_text = loader._run(file_path=file_path)

#     if not contract_text.strip():
#         raise ValueError("Document is empty!")

#     chunks = chunker._run(text=contract_text)
#     os.makedirs('outputs/chunks', exist_ok=True)

#     all_outputs = []


#     for idx, chunk in enumerate(chunks):
#         print(f"Processing chunk {idx + 1}/{len(chunks)}...")
#         output = ChunkProcessor.process_chunk(chunk, chunk_id=idx)
        
#         task_outputs = output

#         print(f"Chunk {idx + 1} processed successfully.", task_outputs, "...")
        
#         # Assuming task_outputs.tasks_output is a list, access the first element
#         if isinstance(task_outputs.tasks_output, list) and len(task_outputs.tasks_output) > 0:
#             task_output = task_outputs.tasks_output[0]
#             real_text = task_output.text if hasattr(task_output, 'text') else str(task_output)

#         else:
#             real_text = ""  # Default to empty if not a list or empty list
        
#         chunk_file = f'outputs/chunks/chunk_{idx+1}.md'
#         with open(chunk_file, 'w', encoding='utf-8') as f:
#             f.write(real_text)
#         all_outputs.append(real_text)

#     # final_risks_summary = ResultMerger.merge_outputs(all_outputs)
#     # risk_text = final_risks_summary

#     # # STEP 1: Ask user about each detected risk
#     # user_decisions = QuestionProcessor.ask_user_for_risks(risk_text)

#     # # STEP 2: Update Contract
#     # updated_contract = ContractUpdaterTool.update_contract(contract_text, user_decisions)

#     # Save updated contract
#     # updated_file_path = 'outputs/updated_contract.md'
#     # with open(updated_file_path, 'w', encoding='utf-8') as f:
#     #     f.write(updated_contract)

#     # print(f"✅ Contract Updated! Saved at {updated_file_path}")

# # def save_output_to_file(output_obj, filepath):
# #     with open(filepath, 'w', encoding='utf-8') as f:
# #         f.write(output_obj.output)

# if __name__ == "__main__":
#     run()





#!/usr/bin/env python
import os
import warnings

from tools.document_loader_tool import DocumentLoaderTool
from tools.document_chunker_tool import DocumentChunkerTool
from processors.chunk_processor import ChunkProcessor
from processors.result_merger import ResultMerger

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    loader = DocumentLoaderTool()
    chunker = DocumentChunkerTool()

    file_path = os.path.join(os.path.dirname(__file__), 'samples', 'confidentiality_agreement.txt')
    contract_text = loader._run(file_path=file_path)

    if not contract_text.strip():
        raise ValueError("Document is empty!")

    chunks = chunker._run(text=contract_text)
    os.makedirs('outputs/chunks', exist_ok=True)

    all_outputs = []

    for idx, chunk in enumerate(chunks):
        print(f"Processing chunk {idx + 1}/{len(chunks)}...")
        output = ChunkProcessor.process_chunk(chunk, chunk_id=idx)
        
        task_outputs = output

        print(f"Chunk {idx + 1} processed successfully.", task_outputs, "...")
        
        if isinstance(task_outputs.tasks_output, list) and len(task_outputs.tasks_output) > 0:
            task_output = task_outputs.tasks_output[0]
            real_text = task_output.text if hasattr(task_output, 'text') else str(task_output)
        else:
            real_text = ""  # Default to empty
        
        chunk_file = f'outputs/chunks/chunk_{idx+1}.md'
        with open(chunk_file, 'w', encoding='utf-8') as f:
            f.write(real_text)
        all_outputs.append(real_text)

    final_risks_summary = ResultMerger.merge_outputs(all_outputs)

    # Save final_risks_summary
    summary_file = 'outputs/final_risks_summary.md'
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(final_risks_summary)

    print(f"✅ Final risks summary saved at: {summary_file}")

if __name__ == "__main__":
    run()
