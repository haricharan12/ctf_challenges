from flask import Flask, request, render_template_string, Response, url_for
import subprocess
import random
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

app = Flask(__name__)

KEY = b'{=18739_docker=}'[:16] 
cipher = AES.new(KEY, AES.MODE_ECB)


def encrypt_endpoint(endpoint: str) -> str:
    
    encoded_bytes = endpoint.encode('utf-8')
    padded_bytes = pad(encoded_bytes, AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_bytes)
    return base64.b64encode(encrypted_bytes).decode('utf-8')

hidden_search_b64 = base64.b64encode(b'hidden_search').decode('utf-8')
quantum_leap_b64 = base64.b64encode(b'quantum_leap').decode('utf-8')

encrypted_hidden_search = encrypt_endpoint(hidden_search_b64)
encrypted_quantum_leap = encrypt_endpoint(quantum_leap_b64)


html_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Chemistry World</title>
    <style>
      body {
        background-color: black;
        color: white;
        font-family: Arial, sans-serif;
        text-align: center;
      }
      .tab { display: none; }
      .tab-buttons { margin: 20px; }
      .tab-buttons button { margin: 0 10px; padding: 10px; font-size: 16px; cursor: pointer; background-color: grey; color: white; border: none; }
      #tab-content { margin-top: 20px; }
      img { max-width: 100%; height: auto; }
    </style>
    <script>
      function showTab(tabId) {
        document.querySelectorAll('.tab').forEach(tab => tab.style.display = 'none');
        document.getElementById(tabId).style.display = 'block';
      }
    </script>
  </head>
  <body onload="showTab('tab1')">
    <h1>Welcome to Chemistry World</h1>
    
    <div class="tab-buttons">
      <button onclick="showTab('tab1')">Metals and Non-Metals</button>
      <button onclick="showTab('tab2')">Organic Chemistry</button>
      <button onclick="showTab('tab3')">Everyday Chemistry</button>
    </div>

    <div id="tab-content">
      <div id="tab1" class="tab">
        <h2>Metals and Non-Metals</h2>
        <p>Metals are elements that are typically hard, shiny, and good conductors of electricity. Did you know that "robots" are often built from various metals due to these properties?</p>
        <p>Non-metals, in contrast, are brittle and poor conductors of electricity, yet essential for creating structures that "robots" can't easily interact with.</p>
        <p>Both metals and non-metals play roles in advancing automation, a key interest of "robots" and their programming.</p>
      </div>

      <div id="tab2" class="tab">
        <h2>Organic Chemistry</h2>
        <p>Organic chemistry studies carbon-containing compounds. Even robots, indirectly, rely on organic compounds for power sources and other materials in their design.</p>
        <p>Life as we know it—and as robots study it—is fundamentally based on these compounds.</p>
        <p>Below is a periodic table with a special embedded key for those exploring hidden files:</p>
        <img src="{{ url_for('static', filename='periodic_table.png') }}" alt="Periodic Table with Embedded Key">
      </div>

      <div id="tab3" class="tab">
        <h2>Everyday Chemistry</h2>
        <p>Chemistry is all around us, even impacting the cleaning products that maintain robots.</p>
        <p>In fact, "robots" often operate in environments managed by chemical processes, including those found in various cleaning agents and preservatives.</p>
        <p>For those adventurous enough, maybe even "robots" might find hidden files revealing more about this topic.</p>
      </div>
    </div>
  </body>
</html>
'''


SPECIAL_KEYWORD = "astatine"


attempt_counter = {}

@app.route('/hidden_search', methods=['GET', 'POST'])
def hidden_search():
    global attempt_counter
    session_id = request.remote_addr  
    attempt_counter[session_id] = attempt_counter.get(session_id, 0) + 1
    random_outputs = [
        "No relevant information found.",
        "Result: Access denied.",
        "Error: Invalid command.",
        "Result: Query unsuccessful.",
        "Searching the archives..."
        "Too close, yet too far!"
    ]
    
    result = ""

    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            if query.lower() == SPECIAL_KEYWORD:
                result = f"You've unlocked the hidden page! Use this encrypted key to find the next endpoint: {encrypted_quantum_leap}"
            else:
                if attempt_counter[session_id] < 5:
                    result = random.choice(random_outputs)
                else:
                    hints = [
                        "Hint: This element is so unstable that it has few practical applications.",
                        "Hint: It’s found at the very end of the halogen group in the periodic table.",
                        "Hint: This element's name starts with 'A'."
                    ]
                    result = random.choice(hints)
    
    return render_template_string(hidden_search_template, result=result)

@app.route('/quantum_leap', methods=['GET', 'POST'])
def quantum_leap():
    result = ""
    if request.method == 'POST':
        query = request.form.get('query').strip()
        
        if query.startswith("ls") or query.startswith("cat"):
            try:
                result = subprocess.check_output(query, shell=True, stderr=subprocess.STDOUT, text=True)
            except subprocess.CalledProcessError:
                result = "Error"  # Generic error message
        else:
            result = "Error: Only 'ls' and 'cat' commands are permitted."

    return render_template_string(quantum_leap_template, result=result)

@app.route('/')
def index():
    return render_template_string(html_template)

# robots.txt route
@app.route('/robots.txt')
def robots_txt():
    robots_content = f"User-agent: *\nDisallow: {encrypted_hidden_search}"
    return Response(robots_content, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
