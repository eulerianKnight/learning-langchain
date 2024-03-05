from dotenv import load_dotenv

from sql import run_query_tool, list_tables, describe_table_tools
from report import write_report_tool

from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate, 
    HumanMessagePromptTemplate, 
    MessagesPlaceholder
)
from langchain.schema import SystemMessage
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory

load_dotenv()

chat = ChatOpenAI()

tables = list_tables()

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=(
            "You are an AI that has access to a SQLite database.\n"
            f"The database has tables of: {tables}\n"
            "Do not make assumptions about what tables exist "
            "or what columns exist. Instead, use the the 'describe_tables' function"
            )),
        MessagesPlaceholder(variable_name="chat_history"), 
        HumanMessagePromptTemplate.from_template("{input}"), 
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [
    run_query_tool,
    describe_table_tools, 
    write_report_tool]

agent = create_openai_functions_agent(
    llm=chat, 
    prompt=prompt, 
    tools=tools)

agent_executor = AgentExecutor(
    agent=agent, 
    verbose=True, 
    tools=tools, 
    memory=memory
)

agent_executor.invoke({"input": "Summarize the top 5 most popular products. Write the results to a report file."})