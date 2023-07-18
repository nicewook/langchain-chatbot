from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from prompt_toolkit import prompt
from rich.console import Console
console = Console()

llm = ChatOpenAI(
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0,
)

conversation = ConversationChain(
    llm=llm,
    memory=ConversationSummaryBufferMemory(llm=ChatOpenAI(), max_token_limit=2048),
    verbose=False,
)

while True:
    print()
    user_input = prompt(console.print("Human: ", style="green"))
    print()

    console.print("AI: ", style="green")
    conversation.run(input=user_input)
    print()

