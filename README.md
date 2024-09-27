Project Overview
Logo Maker is a web application that generates logos based on user input. It uses Natural Language Processing (NLP) to extract keywords and utilizes the OpenAI API to generate custom logo designs.

Installation Instructions
Follow the steps below to run the project locally:
1. Clone the Repository
Clone the project repository to your local machine.
```bash
git clone <repository_url>
```

2. Open the Project in an Editor
Navigate to the project directory and open the project in your preferred code editor (e.g., PyCharm, VS Code, Sublime Text).

 3. Open the Main File
Locate and open the `app1.py` file. This is the main file that runs the Flask application.

4. Create a Templates Folder
In the same directory as `app1.py`, create a folder named `templates`. Inside the `templates` folder, create the following HTML files:
- `login.html`
- `user_input.html`
- `logo_options.html`
These HTML files will handle user login, input, and logo display.

5. Set Up OpenAI API
To generate logos, the project uses the OpenAI API. You need to create an account and obtain an API key.
- Visit [OpenAI](https://beta.openai.com/signup/) and create an account.
- Navigate to the API section and generate an API key.

6. Add API Key
Once you have the API key, open the `app1.py` file and locate the section where the OpenAI API is called. Add your API key in the relevant section of the code.
```python
openai.api_key = "your_api_key_here"
```

7. Run the Project
To run the project, execute the following command in your terminal:
```bash
python app1.py
```
The application will start locally on a development server, and you can access it through your browser.

8. Login Credentials
Use the following credentials to log in:
- Username: vijeth
- Password: admin

Technology Stack
- Backend: Python (Flask)
- Frontend: HTML, CSS, JavaScript
- API: OpenAI API for logo generation

