from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    nova_tarefa = request.json
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    if id < len(tarefas):
        tarefas[id] = request.json
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