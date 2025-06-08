import tkinter as tk
from tkinter import ttk, messagebox
from biblioteca_dados import livros, usuarios, emprestimos, carregar_dados, salvar_dados

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.root.geometry("800x600")
        
        # Carrega os dados e cria a interface
        carregar_dados()
        self.criar_interface()
    
    def criar_interface(self):
        # Barra de menu superior
        menubar = tk.Menu(self.root)
        

        menu_livros = tk.Menu(menubar, tearoff=0)
        menu_livros.add_command(label="Adicionar Livro", command=self.janela_adicionar_livro)
        menu_livros.add_command(label="Listar Livros", command=self.janela_listar_livros)
        menubar.add_cascade(label="Livros", menu=menu_livros)
        

        menu_usuarios = tk.Menu(menubar, tearoff=0)
        menu_usuarios.add_command(label="Adicionar Usuário", command=self.janela_adicionar_usuario)
        menu_usuarios.add_command(label="Listar Usuários", command=self.janela_listar_usuarios)
        menubar.add_cascade(label="Usuários", menu=menu_usuarios)
        
        # Menu Empréstimos
        menu_emprestimos = tk.Menu(menubar, tearoff=0)
        menu_emprestimos.add_command(label="Realizar Empréstimo", command=self.janela_realizar_emprestimo)
        menu_emprestimos.add_command(label="Devolver Livro", command=self.janela_devolver_livro)
        menubar.add_cascade(label="Empréstimos", menu=menu_emprestimos)
        
        self.root.config(menu=menubar)
        
        
        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        
        ttk.Label(self.frame_principal, 
                 text="Biblioteca", 
                 font=('Helvetica', 16)).pack(pady=20)
        
        # Botões principais
        ttk.Button(self.frame_principal, text="Adicionar Livro", 
                  command=self.janela_adicionar_livro).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame_principal, text="Listar Livros", 
                  command=self.janela_listar_livros).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame_principal, text="Adicionar Usuário", 
                  command=self.janela_adicionar_usuario).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame_principal, text="Listar Usuários", 
                  command=self.janela_listar_usuarios).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame_principal, text="Realizar Empréstimo", 
                  command=self.janela_realizar_emprestimo).pack(fill=tk.X, pady=5)
        ttk.Button(self.frame_principal, text="Devolver Livro", 
                  command=self.janela_devolver_livro).pack(fill=tk.X, pady=5)
    
    # Funções para livros
    def janela_adicionar_livro(self):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Livro")
        
        ttk.Label(janela, text="Título:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entrada_titulo = ttk.Entry(janela, width=40)
        entrada_titulo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(janela, text="Autor:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        entrada_autor = ttk.Entry(janela, width=40)
        entrada_autor.grid(row=1, column=1, padx=5, pady=5)
        
        def adicionar():
            titulo = entrada_titulo.get()
            autor = entrada_autor.get()
            
            if not titulo or not autor:
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return
            
            novo_id = max([livro['id'] for livro in livros] or [0]) + 1
            
            novo_livro = {
                "id": novo_id,
                "titulo": titulo,
                "autor": autor,
                "disponivel": True
            }
            
            livros.append(novo_livro)
            salvar_dados()
            messagebox.showinfo("Sucesso", f"Livro '{titulo}' adicionado com sucesso!")
            janela.destroy()
        
        ttk.Button(janela, text="Adicionar", command=adicionar).grid(row=2, column=1, pady=10, sticky=tk.E)
    
    def janela_listar_livros(self):
        janela = tk.Toplevel(self.root)
        janela.title("Lista de Livros")
        janela.geometry("600x400")
        
        if not livros:
            ttk.Label(janela, text="Nenhum livro cadastrado.").pack(padx=10, pady=10)
            return
        
        frame_tabela = ttk.Frame(janela)
        frame_tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Criar Treeview
        colunas = ("id", "titulo", "autor", "disponivel")
        tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")
        
        # Configurar cabeçalhos
        tabela.heading("id", text="ID")
        tabela.heading("titulo", text="Título")
        tabela.heading("autor", text="Autor")
        tabela.heading("disponivel", text="Disponível")
        
        # Configurar colunas
        tabela.column("id", width=50, anchor=tk.CENTER)
        tabela.column("titulo", width=200)
        tabela.column("autor", width=150)
        tabela.column("disponivel", width=80, anchor=tk.CENTER)
        
        # Adicionar dados
        for livro in livros:
            disponivel = "Sim" if livro["disponivel"] else "Não"
            tabela.insert("", tk.END, values=(
                livro["id"], livro["titulo"], livro["autor"], disponivel
            ))
        
        # Adicionar barra de rolagem
        scrollbar = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=tabela.yview)
        tabela.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Funções para usuários
    def janela_adicionar_usuario(self):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Usuário")
        
        ttk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        entrada_nome = ttk.Entry(janela, width=40)
        entrada_nome.grid(row=0, column=1, padx=5, pady=5)
        
        def adicionar():
            nome = entrada_nome.get()
            
            if not nome:
                messagebox.showerror("Erro", "Preencha o nome do usuário!")
                return
            
            novo_id = max([usuario['id'] for usuario in usuarios] or [0]) + 1
            
            novo_usuario = {
                "id": novo_id,
                "nome": nome
            }
            
            usuarios.append(novo_usuario)
            salvar_dados()
            messagebox.showinfo("Sucesso", f"Usuário '{nome}' cadastrado com sucesso!")
            janela.destroy()
        
        ttk.Button(janela, text="Adicionar", command=adicionar).grid(row=1, column=1, pady=10, sticky=tk.E)
    
    def janela_listar_usuarios(self):
        janela = tk.Toplevel(self.root)
        janela.title("Lista de Usuários")
        janela.geometry("400x300")
        
        if not usuarios:
            ttk.Label(janela, text="Nenhum usuário cadastrado.").pack(padx=10, pady=10)
            return
        
        frame_tabela = ttk.Frame(janela)
        frame_tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Criar Treeview
        colunas = ("id", "nome")
        tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")
        
        # Configurar cabeçalhos
        tabela.heading("id", text="ID")
        tabela.heading("nome", text="Nome")
        
        # Configurar colunas
        tabela.column("id", width=50, anchor=tk.CENTER)
        tabela.column("nome", width=300)
        
        # Adicionar dados
        for usuario in usuarios:
            tabela.insert("", tk.END, values=(usuario["id"], usuario["nome"]))
        
        # Adicionar barra de rolagem
        scrollbar = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=tabela.yview)
        tabela.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
