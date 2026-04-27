from langchain_core.messages import HumanMessage,AIMessage
from src.chains.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger=get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city=""
        self.interests=[]
        self.itinerary=""
        
        logger.info("initialized travelplanner instance")
    
    def set_city(self,city:str):
        try:
            self.city=city
            self.messages.append(HumanMessage(content=city))
            logger.info("city set successfully")
        except Exception as e:
            logger.error(f"Error while loading setting city: {e}")
            raise CustomException("Failed to set city ",e)
        
    def set_interests(self,interests_str:str):
        try:
            self.interests= [i.strip() for i in interests_str.split(", ")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("interests also set successfully...")
        except Exception as e:
            logger.error(f"Error while loading setting interests: {e}")
            raise CustomException("Failed to set interests ",e)
        
    def create_itinerary(self):
        try:
            logger.info("generating itinerary for {self.city} and for interests {self.interests}")
            itinerary=generate_itinerary(self.city,self.interests)
            self.itinerary=itinerary
            self.messages.append(AIMessage(content=itinerary))
            logger.info("itinerary generated successfully...")
            return itinerary
        except Exception as e:
            logger.error(f"error while creating itinerary : {e}")
            raise CustomException("Failed to create itinerary ",e)