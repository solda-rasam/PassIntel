from flask import Flask, render_template, request, jsonify
from analyzer import check_pwned_api, calculate_entropy_and_time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get('password', '')
    
    if not password:
        return jsonify({'error': 'Password cannot be empty'}), 400
        
   
    leak_count = check_pwned_api(password)
    entropy, crack_time = calculate_entropy_and_time(password)
    
   
    if leak_count > 0:
        status = "COMPROMISED"
        color = "#ff4a4a"
    elif entropy < 50:
        status = "WEAK"
        color = "#ffb34a"
    else:
        status = "SECURE"
        color = "#4aff8a"

    return jsonify({
        'leak_count': leak_count,
        'entropy': entropy,
        'crack_time': crack_time,
        'status': status,
        'color': color
    })

if __name__ == '__main__':
    app.run(debug=True)