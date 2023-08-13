import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "--"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like. The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!"""

# Generate Random Jokes Function
def generate_joke():
    jokes = [
        "Why You dont  trust atoms? Because they make up everything!, LOLLLL",
        "Parallel lines, It's a shame they'll never meet."
    ]
    return random.choice(jokes)

# This function when called allows to fetch weather through API (My most amazing function out of all).
def get_weather(city):
    # Fetching weather data from an API
    return f"The weather in {city}."

# Generate a fun fact for the user.
def generate_fun_fact():
    facts = [
        "Bananas are berries, but strawberries are not.",
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."
    ]
    return random.choice(facts)

# My tips for the user regarding tech-related tips
def get_tech_tip():
    tips = [
        "Remember to regularly update your software to keep your devices secure.",
        "If your computer is running slow, try clearing temporary files and browser cache.",
        "Use strong, unique passwords for each online account to enhance security."
    ]
    return random.choice(tips)

# My choice of famous landmarks
def get_landmark_info(landmark):
    # Simulate providing information about landmarks THAT I ONLY KNOW
    landmark_info = {
        "eiffel tower": "The Eiffel Tower is a wrought-iron lattice tower in Paris, France. It is one of the most famous landmarks in the world.",
        "statue of liberty": "The Statue of Liberty is a symbol of freedom and democracy in the United States. It is located on Liberty Island in New York Harbor.",
    }
    return landmark_info.get(landmark.lower(), "I'm not aware of the landmark.")


# If user asks for Movie then recomend the following
def recommend_movie(genre):
    if genre.lower() == "action":
        return "I recommend watching 'Inception'."
    elif genre.lower() == "comedy":
        return "You might enjoy 'The Hangover'."
    else:
        return "I'm sorry, I don't have recommendations for that genre."

@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Chatbot logic for responding to user messages"""
    if state is None:
        state = {"counter": 0}

    # To make use and access user's last message
    user_message = message_history[-1].content.lower()

    # Increment the counter
    state["counter"] += 1

    # If weather
    if "weather" in user_message:
        city = user_message.split("weather in")[-1].strip()
        bot_response = get_weather(city)


    # If movie recomendation is asked
    elif "recommend movie" in user_message:
        genre = user_message.split("recommend movie")[-1].strip()
        bot_response = recommend_movie(genre)


    # A standard message for the user
    elif "?" in user_message:
        bot_response = "I'm here to help! Feel free to ask any question."
    else:

        # OpenAI API to generate a response
        bot_response = generate_bot_response(message_history)

    return bot_response, state

def generate_bot_response(message_history: List[Message]) -> str:
    """Generate a response using the OpenAI API"""
    messages = [{"role": msg.role, "content": msg.content} for msg in message_history]

    # Create a payload for the API call
    payload = {
        "messages": messages,
        "system_prompt": SYSTEM_PROMPT,
        "model": "gpt-3.5-turbo"
    }

    # Call the OpenAI API using the messages endpoint
    response = models.OpenAI.call_endpoint("messages", data=payload)

    # Extract the bot response 
    bot_response = response['choices'][0]['message']['content']
    return bot_response
