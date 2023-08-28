from flask import Flask, render_template, request
import openai

app = Flask(__name__)

API_KEY = ''
openai.api_key = API_KEY

def translate_text(text, source_language, target_language):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate the text between the two languages from {source_language} to {target_language} : {text}",
        max_tokens=100
    )

    translated_text = response.choices[0].text.strip().replace('\n', '')
    return translated_text

def clear_translated_text():
    return ""

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        source_language = request.form['source_language']
        target_language = request.form['target_language']
        text_to_translate = request.form['text_to_translate']

        translated_text = translate_text(text_to_translate, source_language, target_language)
        return render_template('index.html', translated_text=translated_text)

    translated_text = clear_translated_text()
    return render_template('index.html', translated_text=translated_text)


if __name__ == '__main__':
    app.run(debug=True)
