import os
import tempfile

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings  # ✅

class AIContractUpdater:
    def __init__(self, model="llama3.2"):
        # LLM: Ollama model like llama3.2
        self.llm = Ollama(model=model, base_url="http://localhost:11434")

        # ✅ Local embedding model via HuggingFace
        self.embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

        # Apply settings globally for LlamaIndex
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model

    def rewrite_contract(self, contract_text: str, user_request: str) -> str:
        # Save contract temporarily
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "contract.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(contract_text)

            # Load and index
            documents = SimpleDirectoryReader(temp_dir).load_data()
            index = VectorStoreIndex.from_documents(documents)

            query_engine = index.as_query_engine(similarity_top_k=3)

            # RAG-enhanced prompt to update relevant clause
            prompt = (
                f"You are a legal contract expert. A user has asked:\n"
                f"'{user_request}'\n"
                f"Please update the relevant clause(s) in the contract to reflect this change. "
                f"Return the full updated contract text."
            )

            response = query_engine.query(prompt)
            return str(response)

# import os
# import tempfile
# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
# from crewai import LLM  # You're already using this in your project

# class AIContractUpdater:
#     def __init__(self, model="llama3.2"):
#         self.llm = LLM(
#             model=model,
#             base_url='http://localhost:11434',
#         )

#         # Set the LLM globally for LlamaIndex
#         # Settings.llm = self.llm

#     def rewrite_contract(self, contract_text: str, user_request: str) -> str:
#         # Step 1: Save the contract to a temporary file
#         with tempfile.TemporaryDirectory() as temp_dir:
#             input_path = os.path.join(temp_dir, "contract.txt")
#             with open(input_path, "w", encoding="utf-8") as f:
#                 f.write(contract_text)

#             # Step 2: Load, index, and query using LlamaIndex + LLM
#             docs = SimpleDirectoryReader(temp_dir).load_data()
#             index = VectorStoreIndex.from_documents(docs)

#             query_engine = index.as_query_engine(similarity_top_k=5)

#             prompt = f"""You are a legal contract expert. A user has asked:
# '{user_request}'
# Please rewrite or modify the relevant clause(s) in the contract accordingly.
# Return the full updated contract."""
            
#             response = query_engine.query(prompt)
#             return str(response)
