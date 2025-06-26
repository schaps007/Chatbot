## FastAPI Chatbot using OpenAI API

This is a simple chatbot API built with **FastAPI** and powered by **OpenAI's GPT model**. The app receives messages via a POST request and responds with AI-generated replies.

### Libraries Used
| Package           | Purpose                               | Install Command                        |
|-------------------|---------------------------------------|----------------------------------------|
| `fastapi`         | Web framework                         | `pip install fastapi`                  |
| `uvicorn`         | ASGI server                           | `pip install uvicorn`                  |
| `pydantic`        | Request validation & parsing          | `pip install pydantic`                 |
| `openai`          | OpenAI GPT API interface              | `pip install openai`                   |
| `python-dotenv`   | Load `.env` variables                 | `pip install python-dotenv`

### Getting Started
1. Open a terminal window and clone the repository using git clone
2. Navigate to the project directory by doing `cd Chatbot`
3. Install the necessary dependencies using the command `pip install -r requirements.txt`
4. Run the server- `uvicorn main:app --reload`
5. Open http://127.0.0.1:8000 and input the OpenAI API key at the top and then you can start sending messages to the chatbot.

### Code Structure
1. `main.py` **(API Layer)**
 - Defines the FastAPI app and /chat endpoint.
 - Uses Pydantic to validate incoming messages.
 - Delegates response generation to chatbot.py.
2. `chatbot.py` **(AI Service Layer)**
 - Loads the OpenAI API key securely from .env.
 - Implements the chatbot_response() function to interact with GPT.
 - Handles errors (e.g., API failures)
