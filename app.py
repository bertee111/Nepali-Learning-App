from flask import Flask, render_template, jsonify, request
from nepali import game, consonants, vowels, dependent_vowels, verbs

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/game', methods=['POST'])
def play_game():
    user_input = request.form.get('playerName')  # Get user input from the form
    # You can process the user_input here as needed
    game_output = f"Hello, {user_input}! Welcome to the game."  # Example output
    return game_output

if __name__ == '__main__':
    app.run(debug=True)