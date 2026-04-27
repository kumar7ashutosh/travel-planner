from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import OPENAI_API_KEY

llm=ChatOpenAI(api_key=OPENAI_API_KEY,model="gpt-4.1",temperature=0.3)

itinerary_prompt=ChatPromptTemplate([
    ("system","You are a helpful travel asssistant. Create a day trip itineary for {city} based on user's interest : {interests}. Provide a brief , bulleted itinerary"),
    ("human" , "Create a itineary for my day trip")
])


def generate_itinerary(city:str,interests:list[str])->str:
    response=llm.invoke(
        itinerary_prompt.format_messages(city=city,interests=', '.join(interests))
    )
    return response.content