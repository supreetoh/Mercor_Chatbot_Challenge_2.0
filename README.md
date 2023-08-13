This AI chatbot has a number of features and can be read about in the following.

# 1. Generate a fun fact:
```bash
generate_fun_fact()
```
This function will generate a random fact based on the prompt by user.
2 responses are encoded further will be called by the OPEN AI API.


# 2. Weather for a place using API: 
```bash 
get_weather(city)
```
The function calls a weather api to provide accurate and real time datat for a location provided.
The API key for the weather data extraction is given by the owner.


# 3. Generate a Joke:
```bash
generate_joke()
```
The function returns a random joke 2 of which encoded by me int the function itself.
If the encoded jokes get exhausted then OPEN AI API fetches for new ones.


# 4. Generate a random Tech-Tip:
```bash
get_tech_tip()
```
Generates random tech related facts for the user.
Contains 3 enocded tips which upon used will fetch from the API.


# 5. Give information about a landmark:
```bash
get_landmark_info(landmark)
```
Returns information related to landmarks when prompted by the user.
If unknown landmark is provided then has a default message for the user.

# 6. Recommend a movie based on Genre
```bash
recommend_movie(genre)
```
A function that recommends movies when the genre is prompted
Has responses for different types of genre.
