from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class DocumentChunkerInput(BaseModel):
    text: str = Field(..., description="Full text to chunk.")

class DocumentChunkerTool(BaseTool):
    name: str = "Document Chunker Tool"
    description: str = "Split big documents into smaller chunks for processing."
    args_schema: Type[BaseModel] = DocumentChunkerInput

    def _run(self, text: str, max_words=500) -> list:
        words = text.split()
        chunks = []
        for i in range(0, len(words), max_words):
            chunk = ' '.join(words[i:i + max_words])
            chunks.append(chunk)
        return chunks
