# Prerequisite

## virtual env

```python
# Create
python3 -m venv langchain-chatbot

# Activate
langchain-chatbot\Scripts\activate # On Windows
source langchain-chatbot/bin/activate. # On Unix or MacOS 

# deactivate
deactivate
```
## Install pacakges

```bash
pip install --upgrade pip
pip -q install openai langchain huggingface_hub transformers
pip freeze > requirements.txt
```