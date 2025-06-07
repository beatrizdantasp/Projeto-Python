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
    
    # Funções para empréstimos
    def janela_realizar_emprestimo(self):
        janela = tk.Toplevel(self.root)
        janela.title("Realizar Empréstimo")
        
        
        livros_disponiveis = [livro for livro in livros if livro["disponivel"]]
        
        if not livros_disponiveis:
            ttk.Label(janela, text="Nenhum livro disponível para empréstimo.").pack(padx=10, pady=10)
            return
        
        if not usuarios:
            ttk.Label(janela, text="Nenhum usuário cadastrado.").pack(padx=10, pady=10)
            return
        
        ttk.Label(janela, text="Livro:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        livro_var = tk.StringVar()
        livro_cb = ttk.Combobox(janela, textvariable=livro_var, width=40, state="readonly")
        livro_cb['values'] = [f"{livro['id']} - {livro['titulo']} ({livro['autor']})" for livro in livros_disponiveis]
        livro_cb.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(janela, text="Usuário:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        usuario_var = tk.StringVar()
        usuario_cb = ttk.Combobox(janela, textvariable=usuario_var, width=40, state="readonly")
        usuario_cb['values'] = [f"{usuario['id']} - {usuario['nome']}" for usuario in usuarios]
        usuario_cb.grid(row=1, column=1, padx=5, pady=5)
        
        def realizar():
            livro_selecionado = livro_var.get()
            usuario_selecionado = usuario_var.get()
            
            if not livro_selecionado or not usuario_selecionado:
                messagebox.showerror("Erro", "Selecione um livro e um usuário!")
                return
            
            livro_id = int(livro_selecionado.split(" - ")[0])
            usuario_id = int(usuario_selecionado.split(" - ")[0])
            
            # Encontra o livro e o usuário
            livro = next(livro for livro in livros if livro["id"] == livro_id)
            usuario = next(usuario for usuario in usuarios if usuario["id"] == usuario_id)
            
            # Cria o empréstimo
            novo_id = max([emp['id'] for emp in emprestimos] or [0]) + 1
            
            novo_emprestimo = {
                "id": novo_id,
                "livro_id": livro_id,
                "usuario_id": usuario_id
            }
            
            emprestimos.append(novo_emprestimo)
            livro["disponivel"] = False
            salvar_dados()
            
            messagebox.showinfo("Sucesso", 
                              f"Empréstimo realizado: {usuario['nome']} pegou '{livro['titulo']}'")
            janela.destroy()
        
        ttk.Button(janela, text="Realizar Empréstimo", command=realizar).grid(row=2, column=1, pady=10, sticky=tk.E)
    
    def janela_devolver_livro(self):
        janela = tk.Toplevel(self.root)
        janela.title("Devolver Livro")
        

        livros_emprestados = []
        for emprestimo in emprestimos:
            livro = next((livro for livro in livros if livro["id"] == emprestimo["livro_id"] and not livro["disponivel"]), None)
            if livro:
                usuario = next((u for u in usuarios if u["id"] == emprestimo["usuario_id"]), None)
                if usuario:
                    livros_emprestados.append({
                        "emprestimo_id": emprestimo["id"],
                        "livro_info": f"{livro['id']} - {livro['titulo']} ({livro['autor']})",
                        "usuario_info": f"{usuario['id']} - {usuario['nome']}"
                    })
         
        if not livros_emprestados:
            ttk.Label(janela, text="Nenhum livro emprestado no momento.").pack(padx=10, pady=10)
            return
        
        ttk.Label(janela, text="Livro emprestado:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        emprestimo_var = tk.StringVar()
        emprestimo_cb = ttk.Combobox(janela, textvariable=emprestimo_var, width=50, state="readonly")
        emprestimo_cb['values'] = [f"ID Empréstimo: {item['emprestimo_id']} | Livro: {item['livro_info']} | Usuário: {item['usuario_info']}" 
                                 for item in livros_emprestados]
        emprestimo_cb.grid(row=0, column=1, padx=5, pady=5)
        
        def devolver():
            selecao = emprestimo_var.get()
            
            if not selecao:
                messagebox.showerror("Erro", "Selecione um empréstimo para devolução!")
                return
            
            emprestimo_id = int(selecao.split("ID Empréstimo: ")[1].split(" |")[0])
            
            # Encontra o empréstimo e marca o livro como disponível
            for emprestimo in emprestimos:
                if emprestimo["id"] == emprestimo_id:
                    livro = next((livro for livro in livros if livro["id"] == emprestimo["livro_id"]), None)
                    if livro:
                        livro["disponivel"] = True
                        salvar_dados()
                        messagebox.showinfo("Sucesso", "Livro devolvido com sucesso!")
                        janela.destroy()
                        return
            
            messagebox.showerror("Erro", "Empréstimo não encontrado.")
        
        ttk.Button(janela, text="Devolver Livro", command=devolver).grid(row=1, column=1, pady=10, sticky=tk.E)

def main():
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()