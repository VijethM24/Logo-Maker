import requests
from flask import Flask, render_template, request, redirect, url_for, session, send_file, Response
import openai
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk, WordNetLemmatizer

app = Flask(__name__)
app.secret_key = 'vijethisthehero'

user_credentials = {
    "vijeth": "admin",
    "admin": "admin",
    "user3": "password3"
}

openai.api_key = "YOUR_API_KEY"

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username in user_credentials and user_credentials[username] == password:
        session["username"] = username
        return redirect(url_for("user_input"))
    else:
        return "Login Failed"


@app.route('/user_input', methods=['GET', 'POST'])
def user_input():
    if request.method == 'POST':
        user_text = request.form.get('user_input')
        logo_urls = generate_logos(user_text)
        session['logo_urls'] = logo_urls
        return redirect(url_for('logo_options'))
    return render_template('user_input.html')


def extract_keywords(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english')) | {'like', 'using', 'would'}
    words = [word for word in tokens if word.isalnum() and word.lower() not in stop_words]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    tagged_words = pos_tag(lemmatized_words)
    named_entities = ne_chunk(tagged_words)

    keywords = [word for word, tag in tagged_words if tag.startswith('NN') or tag in {'JJ', 'VB', 'RB'}]
    for chunk in named_entities:
        if hasattr(chunk, 'label'):
            keywords.append(' '.join(c[0] for c in chunk))
    print("The Extracted keywords are:", keywords)
    return keywords

def generate_logos(text):
    keywords = extract_keywords(text)
    logo_urls = fetch_logos_from_openai(keywords)
    return logo_urls

def fetch_logos_from_openai(keywords):
    try:
        response = openai.Image.create(
            prompt= f"Generate PNG logos of{', '.join(keywords)}",
            n=4,
            size="512x512",
        )
        print("Response from OpenAI:", response) 
        if 'data' not in response:
            raise KeyError("The key 'data' is not found in the response.")
        logo_urls = [data["url"] for data in response['data']]
        return logo_urls
    except Exception as e:
        print("Error while fetching logos from OpenAI:", e)
        return []

@app.route('/logo_options', methods=['GET', 'POST'])
def logo_options():
    if 'logo_urls' not in session:
        return redirect(url_for('user_input'))
    logo_urls = session['logo_urls']
    if request.method == 'POST':
        logo_index = int(request.form.get('logo_index'))
        try:
            response = requests.get(logo_urls[logo_index])
            if response.status_code == 200:
                return Response(
                    response.content,
                    headers={
                        "Content-Disposition": f"attachment; filename=logo_image_{logo_index}.png"
                    },
                    mimetype="image/png"
                )
            else:
                return f"Failed to download image. Status code: {response.status_code}"
        except Exception as e:
            return f"Error downloading image: {e}"
    return render_template('logo_options.html', logo_urls=logo_urls, enumerate=enumerate)

if __name__ == "__main__":
    app.run(debug=True)




