# LangChain

## Chain

- Python Class provided by LangChain.
- Chains are used to make reusable text-generation pipelines.
- Chains can be connected together to make a more complex pipeline.
- A Chain wraps up a PromptTemplate and an LLM.

### PromptTemplate

- Produces the final prompt that will be sent to the language model.
- Must declare the variables it needs to build the prompt.

### LanguageModel

- The LLM we want to to use for for text generation pipeline.
- Can be ChatGPT, Bard, or really anything that produces text.

### Inputs

- Dictionary that must contain values for each variable the PromptTemplate requires.

### Outputs

- Dictionary that contains the inputs and the generated content assigned to the "text" key.

## Chat Model

- A Lot of LangChain assumes we are using a completion model.
- A ton of documentation assumes we are using completion model. Certain classes are designed to work with completion models.
- Using a Chat Model requires just a bit of extra work.

### Memory

- Memory is a class provided by LangChain which is used to store data in a chain.
- Used for lots of things, not just storing the list of messages.
- When we run the chain, the memory receives the input variables and has the ability to add in additional variables.
- After the model runs, the output variables are sent to memory.
- Memory has a chance to inspect the result and store some part of it.
- LangChain has many kinds of memory:
    - ConversationTokenBufferMemory(Completion based LLMs)
    - CombinedMemory(Completion based LLMs)
    - ConversationBufferWindowMemory(Completion based LLMs)
    - ConversationBufferMemory(Chat based LLMs)


## Retriever

- A Retriever is an object that can take in a string and return some relevant documents.
- To be a "Retriever", the object must have a method called "get_relevant_documents" that takes a string and returns a list of documents.


## Agent

- A chain that knows how to use tools.
- It will take that list of tools and convert them into JSON function descriptions.
- It still has input variables, memory, prompts, etc. - all the normal things a chain has.

### AgentExecutor

- Takes an agent and runs it until the response in not a function call
- Essentially a fancy while loop.