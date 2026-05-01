from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

tarefas = []

@app.route('/')
def home():
    return render_template('index.html', tarefas=tarefas)

@app.route('/tarefas_web', methods=['POST'])
def criar_tarefa_web():
    nome = request.form.get('nome')
    status = request.form.get('status')
    prioridade = request.form.get('prioridade')

    tarefas.append({
        "nome": nome,
        "status": status,
        "prioridade": prioridade if prioridade else "normal"
    })

    return redirect('/')

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_tarefa_web(id):
    if id < len(tarefas):
        tarefas.pop(id)
    return redirect('/')


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    nova_tarefa = {
        "nome": request.json.get("nome"),
        "status": request.json.get("status"),
        "prioridade": request.json.get("prioridade", "normal")
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    if id < len(tarefas):
        tarefas[id] = {
            "nome": request.json.get("nome"),
            "status": request.json.get("status"),
            "prioridade": request.json.get("prioridade", "normal")
        }
        return jsonify(tarefas[id])
    return "Tarefa não encontrada", 404

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    if id < len(tarefas):
        tarefa_removida = tarefas.pop(id)
        return jsonify(tarefa_removida)
    return "Tarefa não encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)