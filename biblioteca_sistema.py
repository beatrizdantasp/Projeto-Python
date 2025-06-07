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