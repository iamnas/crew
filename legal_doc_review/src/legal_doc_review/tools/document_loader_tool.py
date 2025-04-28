

# from crewai.tools import BaseTool
# from typing import Type
# from pydantic import BaseModel, Field

# class DocumentLoaderInput(BaseModel):
#     """Input schema for DocumentLoaderTool."""
#     file_path: str = Field(..., description="Path to the legal document text file to load.")

# class DocumentLoaderTool(BaseTool):
#     name: str = "Document Loader Tool"
#     description: str = "Loads the content of a legal document from a local file."
#     args_schema: Type[BaseModel] = DocumentLoaderInput

#     def _run(self, file_path: str) -> str:
#         try:
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 return f.read()
#         except Exception as e:
#             return f"Failed to load document: {e}"



# from crewai.tools import BaseTool
# from typing import Type
# from pydantic import BaseModel, Field
# import os

# # Optional extra imports for PDFs and Word docs
# import textract

# class DocumentLoaderInput(BaseModel):
#     """Input schema for DocumentLoaderTool."""
#     file_path: str = Field(..., description="Path to the legal document file (.txt, .pdf, .docx).")

# class DocumentLoaderTool(BaseTool):
#     name: str = "Document Loader Tool"
#     description: str = "Loads the content of a legal document from a file (.txt, .pdf, .docx)."
#     args_schema: Type[BaseModel] = DocumentLoaderInput

#     def _run(self, file_path: str) -> str:
#         try:
#             ext = os.path.splitext(file_path)[1].lower()

#             if ext == '.txt':
#                 with open(file_path, 'r', encoding='utf-8') as f:
#                     return f.read()

#             elif ext == '.pdf' or ext == '.docx':
#                 # Use textract to handle PDF and DOCX
#                 text = textract.process(file_path)
#                 return text.decode('utf-8')

#             else:
#                 return f"Unsupported file format: {ext}"

#         except Exception as e:
#             return f"Failed to load document: {e}"



from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os

import pdfplumber  # PDF reading
import docx        # DOCX reading

class DocumentLoaderInput(BaseModel):
    file_path: str = Field(..., description="Path to the legal document (.txt, .pdf, .docx)")

class DocumentLoaderTool(BaseTool):
    name: str = "Document Loader Tool"
    description: str = "Loads the content of a legal document (.txt, .pdf, .docx)."
    args_schema: Type[BaseModel] = DocumentLoaderInput

    def _run(self, file_path: str) -> str:
        try:
            ext = os.path.splitext(file_path)[1].lower()

            if ext == '.txt':
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()

            elif ext == '.pdf':
                return self._load_pdf(file_path)

            elif ext == '.docx':
                return self._load_docx(file_path)

            else:
                return f"Unsupported file format: {ext}"

        except Exception as e:
            return f"Failed to load document: {e}"

    def _load_pdf(self, file_path: str) -> str:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    def _load_docx(self, file_path: str) -> str:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
