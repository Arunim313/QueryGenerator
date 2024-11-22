import os
from dotenv import load_dotenv
from querygen.core import QueryGen
from querygen.databases import Sqlite
from querygen.llms import GoogleGenAi
from querygen.vectorstores import ChromaDB

load_dotenv()

api_key = os.getenv('API_KEY')
db_url = os.getenv('DB_URL')
example_path = os.getenv('EXAMPLE_PATH')

# Set up configuration dictionary
config = {'api_key': api_key}

# Create QueryGen instance with configured llm, vectorstore, and database
generators = QueryGen(
    llm=GoogleGenAi(config=config),
    vectorstore=ChromaDB(),
    database=Sqlite()
)

# Create a database connection using the specified URL
conn = generators.database.create_connection(url=db_url)

# Index all Data Definition Language (DDL) statements in the 'main' database into the vectorstore
generators.index_all_ddls(connection=conn, db_name='main')

# Index question-sql pair in bulk from the specified example generator
generators.index(bulk=True, path=example_path)

# Ask a question to the database and visualize the result
response = generators.ask_db(
    question="Show all products whose unit price is more than 30",
    connection=conn,
    visualize=True
)

# Extract and display the chart from the response
chart = response["chart"]
chart.show()
