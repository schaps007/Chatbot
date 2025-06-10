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
3. Install any dependencies (pip install fastapi uvicorn python-dotenv openai)
4. Create a .env file in the root directory and add your OpenAI API key: This is how it should look: OPENAI_API_KEY=(add your key here)
5. Run the server- uvicorn main:app --reload
6. Test via Swagger UI- Open http://127.0.0.1:8000/docs and try out the /chat endpoint.

### Code Flow and Modularization
- `main.py`: Defines the FastAPI app, the /chat endpoint, and the message schema using pydantic. It handles POST requests and delegates chatbot logic.
- `chatbot.py`: Loads the OpenAI API key using dotenv, creates an OpenAI client, and defines the `chatbot_response` function which generates replies using GPT.
