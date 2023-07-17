import os

# from langchain.chains.conversation.memory import ConversationBufferMemory
# from langchain import OpenAI
# from langchain.chains import ConversationChain

# # os.environ['OPENAI_API_KEY'] = 'my apikey' # already in system env
# # print(os.environ['OPENAI_API_KEY'])

# llm = OpenAI(model_name="text-davinci-003", temperature=0, max_tokens=256)

# memory = ConversationBufferMemory()

# conversation = ConversationChain(llm=llm, verbose=True, memory=memory)
# conversation.predict(input="Hi there! I am Sam")

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