from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from dotenv import load_dotenv
load_dotenv()
API = "mongodb://zeeshanalizafar53_db_user:K0Ae9OB2vKrhJOhP@ac-xw9edx7-shard-00-00.laivntp.mongodb.net:27017,ac-xw9edx7-shard-00-01.laivntp.mongodb.net:27017,ac-xw9edx7-shard-00-02.laivntp.mongodb.net:27017/?ssl=true&replicaSet=atlas-j0742x-shard-0&authSource=admin&appName=AI-Database"
client = MongoClient(API)
embedding = GoogleGenerativeAIEmbeddings(model = "models/gemini-embedding-001")
database = client['Restaurant']
collection = database['breakfast']

db = MongoDBAtlasVectorSearch(
    embedding = embedding,
    collection = collection,
    index_name = 'vector_index'

)

menu = [
    "Garlic bread | Starter | AUD $9-15 | 11 am-10 pm",
    "Bruschetta | Starter | AUD $15-27 | 11 am-10 pm",
    "Chicken wings | Starter | AUD $12-22 | 12 pm-10 pm",
    "Calamari | Starter | AUD $18-28 | 12 pm-10 pm",
    "Arancini | Starter | AUD $15-20 | 12 pm-10 pm",
    "Nachos | Starter | AUD $15-25 | 12 pm-10 pm",
    "Mozzarella sticks | Starter | AUD $12-18 | 12 pm-10 pm",
    "Spring rolls | Starter | AUD $10-18 | 11 am-10 pm",
    "Dumplings | Starter | AUD $12-22 | 11 am-10 pm",
    "Salt and pepper squid | Starter | AUD $18-28 | 12 pm-10 pm",
    "Hummus with pita | Starter | AUD $12-20 | 11 am-10 pm",
    "Halloumi cheese | Starter | AUD $16-22 | 11 am-10 pm",
    "Prawn toast | Starter | AUD $14-20 | 12 pm-10 pm",
    "Oysters | Starter | AUD $19-36 | 12 pm-10 pm",
    "Soup of the day | Starter | AUD $12-22 | 11 am-9 pm",
    "Avocado toast | Brunch | AUD $18-28 | 7 am-3 pm",
    "Eggs Benedict | Brunch | AUD $22-30 | 7 am-3 pm",
    "Eggs Florentine | Brunch | AUD $20-28 | 7 am-3 pm",
    "Big breakfast | Breakfast | AUD $25-35 | 7 am-3 pm",
    "Pancakes | Brunch | AUD $18-28 | 7 am-3 pm",
    "Belgian waffles | Brunch | AUD $20-30 | 7 am-3 pm",
    "French toast | Brunch | AUD $18-28 | 7 am-3 pm",
    "Shakshuka | Brunch | AUD $20-29 | 8 am-3 pm",
    "Mushroom toast | Brunch | AUD $18-26 | 7 am-3 pm",
    "Breakfast burrito | Breakfast | AUD $15-24 | 7 am-3 pm",
    "Smoked salmon bagel | Brunch | AUD $17-25 | 7 am-3 pm",
    "Spanish omelette | Breakfast | AUD $22-30 | 7 am-3 pm",
    "Acai bowl | Brunch | AUD $15-23 | 7 am-3 pm",
    "Granola and yoghurt bowl | Breakfast | AUD $12-20 | 7 am-3 pm",
    "Turkish eggs | Brunch | AUD $20-27 | 8 am-3 pm",
    "Fish and chips | Lunch | AUD $20-35 | 11 am-9 pm",
    "Chicken burger | Lunch | AUD $18-28 | 11 am-10 pm",
    "Beef burger | Lunch | AUD $18-30 | 11 am-10 pm",
    "Cheeseburger | Lunch | AUD $18-28 | 11 am-10 pm",
    "Club sandwich | Lunch | AUD $18-26 | 11 am-4 pm",
    "Steak sandwich | Lunch | AUD $20-30 | 11 am-4 pm",
    "Chicken schnitzel | Lunch | AUD $22-32 | 11 am-9 pm",
    "Chicken parmigiana | Lunch | AUD $24-35 | 11 am-9 pm",
    "Margherita pizza | Lunch | AUD $20-27 | 11 am-10 pm",
    "Pepperoni pizza | Lunch | AUD $22-30 | 11 am-10 pm",
    "Chicken Caesar wrap | Lunch | AUD $16-24 | 11 am-4 pm",
    "Beef tacos | Lunch | AUD $18-28 | 11 am-10 pm",
    "Chicken quesadilla | Lunch | AUD $18-27 | 11 am-9 pm",
    "Pad Thai | Lunch | AUD $18-26 | 11 am-9 pm",
    "Chicken fried rice | Lunch | AUD $16-24 | 11 am-9 pm",
    "Scotch fillet steak | Dinner | AUD $40-60 | 5 pm-10 pm",
    "Rib-eye steak | Dinner | AUD $40-65 | 5 pm-10 pm",
    "Beef lasagne | Dinner | AUD $24-35 | 5 pm-10 pm",
    "Spaghetti Bolognese | Dinner | AUD $22-32 | 5 pm-10 pm",
    "Fettuccine Alfredo | Dinner | AUD $22-32 | 5 pm-10 pm",
    "Seafood pasta | Dinner | AUD $30-45 | 5 pm-10 pm",
    "Chicken risotto | Dinner | AUD $25-36 | 5 pm-10 pm",
    "Lamb shank | Dinner | AUD $32-45 | 5 pm-10 pm",
    "Roast chicken | Dinner | AUD $28-40 | 5 pm-10 pm",
    "Grilled barramundi | Dinner | AUD $30-45 | 5 pm-10 pm",
    "Beef short ribs | Dinner | AUD $32-55 | 5 pm-10 pm",
    "Butter chicken | Dinner | AUD $22-32 | 5 pm-10 pm",
    "Lamb curry | Dinner | AUD $22-35 | 5 pm-10 pm",
    "Chicken katsu curry | Dinner | AUD $20-30 | 5 pm-10 pm",
    "Mushroom gnocchi | Dinner | AUD $24-34 | 5 pm-10 pm",
    "Beef stroganoff | Dinner | AUD $25-38 | 5 pm-10 pm",
    "Chicken teriyaki bowl | Dinner | AUD $18-28 | 5 pm-10 pm",
    "Sushi platter | Dinner | AUD $25-45 | 5 pm-10 pm",
    "Seafood paella | Dinner | AUD $30-48 | 5 pm-10 pm",
    "Vegetable curry | Dinner | AUD $20-30 | 5 pm-10 pm",
    "Smoked beef brisket | BBQ | AUD $25-40 | 12 pm-9 pm",
    "Beef short rib | BBQ | AUD $30-55 | 12 pm-10 pm",
    "BBQ pork ribs | BBQ | AUD $28-45 | 12 pm-10 pm",
    "BBQ chicken wings | BBQ | AUD $15-25 | 12 pm-10 pm",
    "Grilled lamb chops | BBQ | AUD $30-45 | 12 pm-10 pm",
    "Beef kebabs | BBQ | AUD $22-35 | 12 pm-10 pm",
    "Chicken skewers | BBQ | AUD $20-32 | 12 pm-10 pm",
    "Mixed grill platter | BBQ | AUD $35-65 | 12 pm-10 pm",
    "Korean BBQ meat selection | BBQ | AUD $40-60 per person | 12 pm-10:30 pm",
    "Grilled prawns | BBQ | AUD $25-40 | 12 pm-10 pm",
    "BBQ pork belly | BBQ | AUD $25-40 | 12 pm-10 pm",
    "Smoked sausage platter | BBQ | AUD $20-35 | 12 pm-10 pm",
    "Grilled barramundi | BBQ | AUD $28-42 | 12 pm-10 pm",
    "BBQ mushroom skewers | BBQ | AUD $16-25 | 12 pm-10 pm",
    "Smoked meat sharing platter | BBQ | AUD $45-90 | 12 pm-10 pm",
    "Caesar salad | Salad | AUD $17-25 | 11 am-9 pm",
    "Greek salad | Salad | AUD $16-24 | 11 am-9 pm",
    "Garden salad | Salad | AUD $12-20 | 11 am-9 pm",
    "Chicken avocado salad | Salad | AUD $20-29 | 11 am-9 pm",
    "Quinoa salad | Salad | AUD $17-25 | 11 am-9 pm",
    "Caprese salad | Salad | AUD $18-26 | 11 am-9 pm",
    "Poke bowl | Salad | AUD $18-28 | 11 am-9 pm",
    "Falafel bowl | Salad | AUD $17-25 | 11 am-9 pm",
    "Flat white | Drink | AUD $4-6 | 7 am-5 pm",
    "Cappuccino | Drink | AUD $4-6 | 7 am-5 pm",
    "Iced latte | Drink | AUD $5-8 | 7 am-5 pm",
    "Fresh orange juice | Drink | AUD $6-10 | 7 am-9 pm",
    "Smoothie | Drink | AUD $8-13 | 7 am-5 pm",
    "Milkshake | Drink | AUD $7-12 | 10 am-10 pm",
    "Iced chocolate | Drink | AUD $7-12 | 10 am-10 pm",
    "Chocolate brownie | Other - Dessert | AUD $10-16 | 11 am-10 pm",
    "Tiramisu | Other - Dessert | AUD $12-16 | 12 pm-10 pm",
    "Basque cheesecake | Other - Dessert | AUD $12-17 | 11 am-10 pm",
    "Sticky date pudding | Other - Dessert | AUD $12-17 | 12 pm-10 pm",
    "Ice cream sundae | Other -  Dessert | AUD $9-15 | 11 am-10 pm "
]

# db.add_texts(menu)
retriever = db.as_retriever(
    search_kwargs={
        'k':20
    }
)
result = retriever.invoke("give me starters")
for doc in result:
    print(doc.page_content)