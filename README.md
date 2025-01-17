# 🧠 QueryGenerator

QueryGen is a Python RAG (Retrieval-Augmented Generation) Library designed to streamline the interaction between users and their databases using just a few lines of code. With seamless integration for renowned databases such as PostgreSQL, MySQL, and SQLite, QueryGen also extends its capabilities to major databases like Snowflake and BigQuery by extending the `Database` Interfaces. This library utilizes large language models (LLM) like GPT-4, Llama 2, Google Gemini, and supports knowledge bases like ChromaDB and Faiss.

![QueryGen Chart](https://github.com/Arunim313/QueryGin/blob/main/assets/FLOW.png)

## 🚀 Installation

To install QueryGen, you can use pip:

```commandline
pip install QueryGenerator
```

QueryGen requires Python 3.10 or higher.

## 💡 Usage
```python
# !pip install QueryGenerator

from QueryGen.core import QueryGenCore
from QueryGen.databases import Sqlite
from QueryGen.llms import GoogleGenAi
from QueryGen.vectorstores import ChromaDB

# Add Your Configurations
config = {"api_key": "YOUR-API-KEY"}

# Choose the Vector Store. LLM and DB You Want to Work With And
# Create QueryGenCore Instance With Configured Llm, Vectorstore, And Database
generator = QueryGenCore(
    llm=GoogleGenAi(config=config),
    vectorstore=ChromaDB(),
    database=Sqlite()
)

# Create a Database Connection Using The Specified URL
connection = generator.database.create_connection(url="YOUR_DATABASE_CONNECTION_URL")

# Index All Data Definition Language (DDL) Statements in The Specified Database Into The Vectorstore
generator.index_all_ddls(connection=connection, db_name='NAME_OF_THE_DB')

# Index Question-Sql Pair in Bulk From the Specified Example Path
generator.index(bulk=True, path="your-qsn-sql-example.json")

# Ask a Question to The Database And Visualize The Result
response = generator.ask_db(
    question="YOUR_QUESTION",
    connection=connection,
    visualize=True
)

# Extract And Display The Chart From The Response
chart = response["chart"]
chart.show()

# Close The Connection to Your DB
connection.close()
```
## 📁 Code Structure 

- **_utils:** Utility modules containing constants and a logger.
- **_helper:** The helper module.
- **core:** The main core module, `generator_core.py`.
- **databases:** Database-related modules.
- **llms:** Modules related to Language Models.
- **testing:** Testing scripts.
- **vectorstores:** Modules related to vector stores.
- **poetry.lock** and **pyproject.toml:** Poetry dependencies and configuration files.
- **tests:** Testcases.

## 🤝 Contributing Guidelines 

Thank you for considering contributing to our project! Please follow these guidelines for smooth collaboration:

1. Fork the repository and create your branch from master.
2. Ensure your code adheres to our coding standards and conventions.
3. Test your changes thoroughly and add a test case in the `tests` folder.
4. Submit a pull request with a clear description of the problem and solution.

   [Learn more](CONTRIBUTING.md)

## 🐛 Bug Reports

If you encounter a bug while using QueryGen, help us resolve it by following these steps:

1. Check existing issues to see if the bug has been reported.
2. If not, open a new issue with a detailed description, including steps to reproduce and relevant screenshots or error messages.
   
     [Learn more](.github/ISSUE_TEMPLATE/bug-report.md)

##  🚀 Feature Requests

We welcome suggestions for new features or improvements to QueryGen. Here's how you can request a new feature:

1. Check existing feature requests to avoid duplication.
2. If your feature request is unique, open a new issue and describe the feature you would like to see.
3. Provide as much context and detail as possible to help us understand your request.

    [Learn more](.github/ISSUE_TEMPLATE/feature-request.md)

## 📣 Feedback

We value your feedback and strive to improve QueryGen. Here's how you can share your thoughts with us:

- Open an issue to provide general feedback, suggestions, or comments.
- Be constructive and specific in your feedback to help us understand your perspective better.

Thank you for your interest in contributing to our project! We appreciate your support and look forward to working with you. 🚀



