# ⚖️ Legal Document Review Assistant

This project is a multi-agent, RAG-powered CLI assistant that can:

- ✅ Extract clauses, detect risks, and summarize legal contracts
- ✅ Allow users to interactively request contract updates (like "extend term to 5 years")
- ✅ Rewrite the document using LLMs like `llama3.2` or `mistral` (via Ollama)
- ✅ Work fully offline with local models

---

## 🧪 Example Use Cases

- Review NDAs, employment or SaaS agreements
- Update confidentiality duration or termination notice
- Chatbot-style interaction to update clauses in natural language

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/legal-doc-review
cd legal-doc-review
```

### 2. Create Conda Environment

```bash
conda create -n master-crewai-course python=3.11
conda activate master-crewai-course
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install crewai llama-index langchain langchain-community langchain_ollama langchain_huggingface google-generativeai
pip install sentence-transformers
```

---

## 🤖 LLM Setup (Ollama)

Make sure Ollama is installed and running:

```bash
ollama run llama3:latest
```

For smaller models:
```bash
ollama run mistral
```

---

## 🧾 Run Main Pipeline (Clause Extraction + Summary)

```bash
python src/legal_doc_review/main.py
```

---

## 💬 Run the Chatbot (Interactive Updates)

```bash
python src/legal_doc_review/chatbot.py
```

You’ll be prompted for a file in the `samples/` directory like:

```
legal_document.txt
nda_sample.txt
employment_agreement_sample.txt
```

You'll then be able to type update requests like:

- “Extend the term to 5 years”
- “Add a severance clause”
- “Clarify non-compete language”

---

## 📁 Project Structure

```
src/legal_doc_review/
├── main.py               # End-to-end pipeline runner
├── chatbot.py            # CLI-based contract editor assistant
├── tools/                # Custom tools for LLM, loader, updater
├── processors/           # Chunk processor, merger, question-asker
├── samples/              # Input contracts to analyze and edit
├── outputs/              # Final updated contracts and logs
```

---

## 🔍 Troubleshooting

- ❗ **Slow responses?** Try smaller model like `mistral`
- ❗ **Not recognizing valid request?** Phrase more directly, like "Change term clause"
- ❗ **Ollama not responding?** Make sure it's running and model is preloaded

---

## 🙌 Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [LangChain](https://www.langchain.com/)
- [LlamaIndex](https://www.llamaindex.ai/)
- [Ollama](https://ollama.com/)
- [Sentence-Transformers](https://www.sbert.net/)

---

## 📜 License

MIT License — use freely and ethically.
