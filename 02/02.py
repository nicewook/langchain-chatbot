from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from prompt_toolkit import prompt

from rich.console import Console
console = Console()

llm = ChatOpenAI()
conversation = ConversationChain(
    llm=llm,
    memory=ConversationSummaryBufferMemory(
        llm=ChatOpenAI(), max_token_limit=2048
    ),
    verbose=False,
)

while True:
  user_input = prompt(console.print('Human: ', style="green"))
  print()
  
  result = conversation.predict(input=user_input)
  print(console.print('AI: ', style="green"), result)
  print()