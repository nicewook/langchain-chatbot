from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory

llm = ChatOpenAI()
conversation = ConversationChain(
    llm=llm,
    memory=ConversationSummaryBufferMemory(
        llm=ChatOpenAI(), max_token_limit=2048
    ),
    verbose=False,
)

while True:
  user_input = input("Human: ")
  result = conversation.predict(input=user_input)
  print("AI:", result)