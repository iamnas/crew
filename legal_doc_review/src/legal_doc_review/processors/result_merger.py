class ResultMerger:
    @staticmethod
    def merge_outputs(chunk_outputs: list) -> str:
        return "\n\n---\n\n".join(chunk_outputs)
