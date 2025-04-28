from crew import LegalDocReview

class ChunkProcessor:
    @staticmethod
    def process_chunk(chunk_text, chunk_id):
        inputs = {'legal_document': chunk_text}
        result = LegalDocReview().crew().kickoff(inputs=inputs)
        print(f"Chunk {chunk_id + 1} processed successfully.",result)
        return result
