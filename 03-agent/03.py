# LLM related
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.tools import DuckDuckGoSearchRun

# utilities
from prompt_toolkit import prompt
from rich.console import Console

console = Console()

# Code
# 1. 메모리, LLM, 툴 세가지를 정의한다.
memory = ConversationBufferMemory(
    memory_key="chat_history", # 이 값이 필수이다. 왜 그럴까?
    return_messages=True,
)
llm = ChatOpenAI(
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0,
)
search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world",
    ),
]
# 2. 위 셋을 조합하여 에이전트를 정의한다.
agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
)

# print all
while True:
    print()
    user_input = prompt(console.print("Human: ", style="green"))
    print()

    console.print("AI: ", style="green")
    result = agent_chain.run(input=user_input)
    print(result)

# if you want only final output of agent stream
# https://python.langchain.com/docs/modules/agents/how_to/streaming_stdout_final_only