

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class DocumentLoaderInput(BaseModel):
    """Input schema for DocumentLoaderTool."""
    file_path: str = Field(..., description="Path to the legal document text file to load.")

class DocumentLoaderTool(BaseTool):
    name: str = "Document Loader Tool"
    description: str = "Loads the content of a legal document from a local file."
    args_schema: Type[BaseModel] = DocumentLoaderInput

    def _run(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Failed to load document: {e}"
