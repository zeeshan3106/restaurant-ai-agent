from langgraph.graph import StateGraph, START,END
from typing import TypedDict, Literal
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
import sqlite3
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse, StreamingResponse
from langgraph.config import get_stream_writer
from fastapi.middleware.cors import CORSMiddleware
import time
import os

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")
API = os.getenv("MONGODB_URI")

embeding = GoogleGenerativeAIEmbeddings(model = "models/gemini-embedding-001")
client = MongoClient(API)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
class State(TypedDict):
    query:str
    course:Literal['breakfast', 'lunch','dinner','brunch','bbq','starters','salad','drinks','curry','chinesefood','gelato','seafood','Hi']
    breakfast:str
    lunch:str
    dinner:str
    brunch:str
    bbq:str
    starters:str
    salad:str
    drinks:str
    curry:str
    chinesefood:str
    seafood:str
    gelato:str

class Courses(TypedDict):
    course:Literal['breakfast', 'lunch','dinner','brunch','bbq','starters','salad','drinks','curry','chinesefood','gelato','seafood','Hi']
 


def Course(State:State):
    query = State['query']
    prompt = f" This is the query of the individual select from which category this query belongs"
    smodel = model.with_structured_output(Courses)
    result = smodel.invoke(prompt)
    State['course']=result['course']

    return {
        'course':result['course']
    }

def Breakfast(State:State):
    writer = get_stream_writer()
    collect = State['course']
    database = client['Restaurant']
    query = State['query']
    collection = database['breakfast']
    db = MongoDBAtlasVectorSearch(
        embedding= embeding,
        collection= collection,
        index_name = 'vector_index'

    )
    retriever = db.as_retriever(
        search_kwargs={
            'k':20
        }
    )
    result = retriever.invoke(query)
    knowledge = []
    for i in result:
        knowledge.append(i.page_content)




    


    prompt = f"""this is the query{query} of the customer this is the RAG KnowledgeBAse{knowledge} ans the question to the user
    
    
    only when user say Hi (if user say Hi only ask for category and present one or two items) otherwise no
    Rules:
- Always use green tick emoji for one time atleast not too much
- Use other emojis relates to data but ocasionally not which all
- Always use green tick emoji for one time atleast not too much
- Do not use Markdown.
- Do not use asterisks (*) for bold or bullet points.
- Do not use headings with Markdown formatting.
- Respond in plain text with clean spacing

always ask a question from the user in the ed relates to the stuff

    
    
    
     """
    answer = []

    for chunk in model.stream(prompt):
        for block in chunk.content:
            if block.get('type') == 'text' and block.get('text'):
                text = block['text']
                answer.append(text)
                for word in text.split(' '):
                    writer(word + ' ')
                    time.sleep(0.03)

    return {'answer': ''.join(answer)}
    






graph = StateGraph(State)
graph.add_node('breakfast',Breakfast)
graph.add_node('course',Course)
graph.add_edge(START, 'course')
graph.add_edge('course', 'breakfast')
graph.add_edge('breakfast', END)
workflow = graph.compile()

@app.post('/Agent')
def API(Query:str = Body(...)):
    config = {'configurable':{'thread_id':1}}
    initial_state ={'query':Query}
    return StreamingResponse(
        (
            chunk
            for chunk in workflow.stream(
                initial_state,
        
                stream_mode='custom'
            )

            if isinstance(chunk, str)
        ),
        media_type='text/plain'
    )
   


   




    


  




