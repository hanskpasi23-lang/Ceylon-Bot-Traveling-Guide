from flask import Flask, request, jsonify, session, send_from_directory
import database
from inference import ChatbotEngine

app = Flask(__name__, static_folder='static')
app.secret_key = 'super_secret_sri_lanka_key'

database.init_db()
engine = ChatbotEngine()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/admin')
def admin():
    return send_from_directory(app.static_folder, 'admin.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').strip()
    if not user_message:
        return jsonify({"text": "Please say something.", "emotion": "neutral"})

    if session.get('learning_state'):
        pending_question = session.get('pending_question')
        if not pending_question:
            session['learning_state'] = False
            return jsonify(engine.get_response(user_message))
        response = engine.learn(pending_question, user_message)
        session['learning_state'] = False
        session['pending_question'] = None
        return jsonify(response)

    response = engine.get_response(user_message)
    if response.get('learning'):
        session['learning_state'] = True
        session['pending_question'] = user_message
    return jsonify({"text": response['text'], "emotion": response['emotion']})

# ---- Admin API ----
@app.route('/api/packages', methods=['GET'])
def api_get_packages():
    return jsonify(database.get_packages_with_ids())

@app.route('/api/packages', methods=['POST'])
def api_add_package():
    d = request.json
    database.add_package(d['name'], d['destination'], d['description'], d['price'], d['duration'], d.get('category', 'General'))
    engine.train_model()
    return jsonify({"status": "ok"})

@app.route('/api/packages/<int:pid>', methods=['DELETE'])
def api_delete_package(pid):
    database.delete_package(pid)
    engine.train_model()
    return jsonify({"status": "ok"})

@app.route('/api/knowledge', methods=['GET'])
def api_get_knowledge():
    return jsonify(database.get_domain_knowledge_with_ids())

@app.route('/api/knowledge', methods=['POST'])
def api_add_knowledge():
    d = request.json
    database.add_domain_knowledge(d['question'], d['answer'], d.get('category', 'general'), d.get('keywords', ''))
    engine.train_model()
    return jsonify({"status": "ok"})

@app.route('/api/knowledge/<int:kid>', methods=['DELETE'])
def api_delete_knowledge(kid):
    database.delete_domain_knowledge(kid)
    engine.train_model()
    return jsonify({"status": "ok"})

@app.route('/api/learned', methods=['GET'])
def api_get_learned():
    return jsonify(database.get_learned_qa_with_ids())

@app.route('/api/learned/<int:lid>', methods=['DELETE'])
def api_delete_learned(lid):
    database.delete_learned_qa(lid)
    engine.train_model()
    return jsonify({"status": "ok"})

@app.route('/api/retrain', methods=['POST'])
def api_retrain():
    engine.train_model()
    return jsonify({"status": "ok", "corpus_size": len(engine.corpus)})

if __name__ == '__main__':
    print("Starting Tour Planning Assistant Server...")
    app.run(debug=True, port=5000)
