from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Работает!"

# УБЕРИ ЭТО или закомментируй:
# if __name__ == '__main__':
#     app.run(debug=True)  # <-- ЭТО ПРОБЛЕМА!

# ВМЕСТО ЭТОГО добавь в самый конец:
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False важно!