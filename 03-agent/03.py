# LLM related
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# utilities
from prompt_toolkit import prompt
from rich.console import Console
console = Console()

# Code

chat = ChatOpenAI(
    temperature=0,
)

messages = [
    HumanMessage(
        content="How do you compare to gpt-4?"
    )
]
result = chat(messages)
print(result.content)


