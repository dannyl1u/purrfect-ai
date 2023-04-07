# 💻 Mountain Madness Hackathon 2023 💻 
# Rubey on Tails 🐕

VIDEO DEMO: https://youtu.be/psBENhE4XDA

This web app generates funny pet names for all kinds of animals, making POST requests to the OpenAI API that generates a pet name using Natural Language Processing. It makes additional GET requests to another API (node-server), which makes GET requests to another API (french-translator-server) which takes in the AI generated pet name and translates it to a newly invented language, known as French++. 

<img width="1461" alt="image" src="https://user-images.githubusercontent.com/45186464/219979972-59ef1fd2-7368-43fc-a0c3-92de37b8a5e0.png">

Rubey - a complicated solution to a simple problem. 

<img width="600" alt="image" src="https://user-images.githubusercontent.com/45186464/219985536-2795d20d-ee00-40c7-bca1-56ce1b8c83e1.png">

<!-- ![image](https://user-images.githubusercontent.com/45186464/219985536-2795d20d-ee00-40c7-bca1-56ce1b8c83e1.png) -->


## Setup user app

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone the user app repository, and navigate to the project directory
   ```bash
   $ git clone https://github.com/dannyl1u/pet-name-generator-service.git
   $ cd pet-name-generator-service
   ```



3. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

4. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

5. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

6. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

7. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)

## Now we need to setup our backend servers for the app to work:

Node Server
https://github.com/dannyl1u/node-server

1. Clone the repository

   ```bash
   $ git clone https://github.com/dannyl1u/node-api.git
   ```

2. Navigate into the project directory

   ```bash
   $ cd node-api
   ```

3. run npm install

   ```bash
   $ npm install
   ```

4. Run the server

   ```bash
   $ node .
   ```

Server should now be up at [http://localhost:8080](http://localhost:8080)

# French translater Server
https://github.com/dannyl1u/french-translator-server
1. Clone the repository and navigate to the directory

   ```bash
   $ git clone https://github.com/dannyl1u/french-translator-server.git
   $ cd french-translator-server
   ```

2. Ensure python is installed.

   ```bash
   $ python --version
   ```
3. Install flask

   ```bash
   $ pip install Flask
   # we might need to replace pip with pip3
   # this also requires that pip is installed
   $ pip --version
   ```

4. Run the server

   ```bash
   $ python api.py
   ```
   
 Server should now be up at [http://localhost:8000](http://localhost:8000)

## All done. Head back to the user app at [http://localhost:5000](http://localhost:5000) and generate your pet name!
