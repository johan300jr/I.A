from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        message = request.form['message']
        response = generate_response(message)
        return render_template('chat.html', message=message, response=response)
    else:
        return render_template('chat.html')

import openai

openai.api_key = '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'

def generate_response(message):
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=3097,
        n=1,
        stop=None,
        temperature=0.2
    )
    response = completion.choices[0].text.strip()
    return response

if __name__ == '__main__':
    app.run(debug=True)
