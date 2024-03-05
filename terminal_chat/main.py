from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory, ConversationSummaryMemory

load_dotenv()

chat = ChatOpenAI(verbose=True)

# memory = ConversationBufferMemory(
#     chat_memory=FileChatMessageHistory("messages.json"),
#     memory_key="messages", 
#     return_messages=True)

memory = ConversationSummaryMemory(
    memory_key="messages", 
    return_messages=True, 
    llm=chat
)

prompt = ChatPromptTemplate(
    input_variables=["content"], 
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat, 
    prompt=prompt, 
    memory=memory, 
    verbose=True
)

while True:
    content = input(">> ")
    result = chain.invoke({"content": content})

    print(result['text'])