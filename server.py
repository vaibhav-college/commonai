from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>CommonAI UI</title></head>
<body>
    <h1>CommonAI Inference</h1>
    <form action="/send_prompt" method="POST">
        <textarea name="prompt" rows="5" cols="40"></textarea><br>
        <button type="submit">Generate</button>
    </form>
    {% if prompt %}
        <h3>Prompt:</h3><p>{{ prompt }}</p>
        <h3>Output:</h3><p>{{ generated_text }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    prompt = request.form['prompt']
    response = requests.post("http://localhost:5001/forward_pass", data={"prompt": prompt})
    return render_template_string(HTML_TEMPLATE, prompt=prompt, generated_text=response.text)

if __name__ == '__main__':
    app.run(port=5000)
