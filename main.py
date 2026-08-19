import os
from dotenv import load_dotenv
load_dotenv(".env")
api_key = os.getenv("API_KEY")
db_url = os.getenv("DATABASE_URL")

print("this is for the test")
print("This is a test print statement")

print("for test2")
