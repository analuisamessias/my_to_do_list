class TaskManager:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def adicionar_tarefa(self, descricao):
        if not descricao or not descricao.strip():
            raise ValueError("A descrição da tarefa não pode ser vazia.")
        tarefa = {"id": self.proximo_id, "descricao": descricao.strip(), "concluída": False}
        self.tarefas.append(tarefa)
        self.proximo_id += 1
        return tarefa

    def listar_tarefas(self, apenas_concluidas=None):
        if apenas_concluidas is None:
            return self.tarefas
        return [t for t in self.tarefas if t["concluída"] == apenas_concluidas]

    def concluir_tarefa(self, id_tarefa):
        for t in self.tarefas:
            if t["id"] == id_tarefa:
                t["concluída"] = True
                return t
        raise ValueError("Tarefa não encontrada.")

    def remover_tarefa(self, id_tarefa):
        for t in self.tarefas:
            if t["id"] == id_tarefa:
                self.tarefas.remove(t)
                return True
        raise ValueError("Tarefa não encontrada.")

    def limpar_tarefas_concluidas(self):
        self.tarefas = [t for t in self.tarefas if not t["concluída"]]
        return self.tarefas
    
    def editar_tarefa(self, id_tarefa, nova_desc):
        if not nova_desc or not nova_desc.strip():
            raise ValueError("Nova descrição inválida.")

        for t in self.tarefas:
            if t["id"] == id_tarefa:
                t["descricao"] = nova_desc.strip()
                return t
        raise ValueError("Tarefa não encontrada.")
