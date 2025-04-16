from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

memory = ConversationBufferMemory(return_messages=True)

chat_agent = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)
