import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from to_do_list.task import TaskManager

@pytest.fixture
def manager():
    return TaskManager()

def test_adicionar_tarefa(manager):
    t = manager.adicionar_tarefa("Estudar para a prova de Redes")
    assert t["descricao"] == "Estudar para a prova de Redes"
    assert not t["concluída"]

def test_nao_permite_tarefa_vazia(manager):
    with pytest.raises(ValueError):
        manager.adicionar_tarefa("   ")

def test_concluir_tarefa(manager):
    t = manager.adicionar_tarefa("Treino superiores")
    manager.concluir_tarefa(t["id"])
    assert manager.tarefas[0]["concluída"] is True

def test_remover_tarefa(manager):
    t = manager.adicionar_tarefa("Trabalho prático de ES-II")
    ok = manager.remover_tarefa(t["id"])
    assert ok
    assert len(manager.tarefas) == 0

def test_limpar_tarefas_concluidas(manager):
    manager.adicionar_tarefa("TCC - Montar Banco de Dados")
    t2 = manager.adicionar_tarefa("Estudar Algoritmos")
    manager.concluir_tarefa(t2["id"])
    manager.limpar_tarefas_concluidas()
    assert len(manager.tarefas) == 1
    assert manager.tarefas[0]["descricao"] == "TCC - Montar Banco de Dados"

def test_listar_tarefas_filtradas(manager):
    manager.adicionar_tarefa("Montar Apresentação Pitch")
    t2 = manager.adicionar_tarefa("Montar Poster final")
    manager.concluir_tarefa(t2["id"])
    concluidas = manager.listar_tarefas(apenas_concluidas=True)
    pendentes = manager.listar_tarefas(apenas_concluidas=False)
    assert len(concluidas) == 1
    assert len(pendentes) == 1
  
def test_ids_incrementam(manager):
    t1 = manager.adicionar_tarefa("Aula prática 4")
    t2 = manager.adicionar_tarefa("Aula prática 5")
    assert t2["id"] == t1["id"] + 1

def test_listar_tarefas_concluidas(manager):
    manager.adicionar_tarefa("Aula prática 4")
    t = manager.adicionar_tarefa("Aula prática 5")
    manager.concluir_tarefa(t["id"])
    concluidas = manager.listar_tarefas(apenas_concluidas=True)
    assert len(concluidas) == 1
    assert concluidas[0]["descricao"] == "Aula prática 5"

def test_remover_inexistente(manager):
    manager.adicionar_tarefa("Aula prática 4")
    with pytest.raises(ValueError):
        manager.remover_tarefa(99)

