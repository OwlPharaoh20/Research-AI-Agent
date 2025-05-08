from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic 

load_dotenv() 


llm = ChatAnthropic(model="clade-3-5-sonnet-20241022")
response = llm.invoke("What is the meaning of life?")
print(response)