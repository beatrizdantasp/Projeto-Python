import json
import os

ARQUIVO_DADOS = "biblioteca_dados.json"

def carregar_dados():
    """Carrega os dados do arquivo JSON"""
    global livros, usuarios, emprestimos
    
    
    livros = []
    usuarios = []
    emprestimos = []
    
    if not os.path.exists(ARQUIVO_DADOS):
        return
    
    try:
        with open(ARQUIVO_DADOS, "r") as f:
            dados = json.load(f)
            livros = dados.get("livros", [])
            usuarios = dados.get("usuarios", [])
            emprestimos = dados.get("emprestimos", [])
    except (json.JSONDecodeError, FileNotFoundError):
        pass

def salvar_dados():
    """Salva os dados em um arquivo JSON"""
    dados = {
        "livros": livros,
        "usuarios": usuarios,
        "emprestimos": emprestimos
    }
    
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump(dados, f, indent=4)


carregar_dados()