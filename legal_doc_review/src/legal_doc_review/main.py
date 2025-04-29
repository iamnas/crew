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

    file_path = os.path.join(os.path.dirname(__file__), 'samples', 'saas_agreement.txt')
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
