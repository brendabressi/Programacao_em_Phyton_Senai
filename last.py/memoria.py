import tkinter as tk
import random
import time

class JogoMemoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Memória com Números")
        self.root.geometry("500x300")
        
        # Configurações iniciais
        self.sequencia = []
        self.pontuacao = 0
        self.nivel = 1
        self.tempo_limite = 5
        
        # Interface Gráfica
        self.label_titulo = tk.Label(root, text="Jogo da Memória com Números", font=("Arial", 16))
        self.label_titulo.pack(pady=20)
        
        self.label_instrucoes = tk.Label(root, text="Memorize a sequência de números", font=("Arial", 12))
        self.label_instrucoes.pack(pady=5)
        
        self.label_sequencia = tk.Label(root, text="", font=("Arial", 20))
        self.label_sequencia.pack(pady=20)
        
        self.entry_resposta = tk.Entry(root, font=("Arial", 14))
        self.entry_resposta.pack(pady=5)
        
        self.botao_enviar = tk.Button(root, text="Enviar", command=self.checar_resposta, font=("Arial", 12), bg="green", fg="white")
        self.botao_enviar.pack(pady=10)
        
        self.label_feedback = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.label_feedback.pack(pady=10)
        
        self.label_pontuacao = tk.Label(root, text="Pontuação: 0", font=("Arial", 12))
        self.label_pontuacao.pack(pady=5)
        
        self.label_rodada = tk.Label(root, text="Nível: 1", font=("Arial", 12))
        self.label_rodada.pack(pady=5)

        # Começa o jogo
        self.iniciar_nivel()

    def iniciar_nivel(self):
        """ Função para iniciar um novo nível """
        self.sequencia.append(random.randint(0, 9))  # Adiciona um novo número aleatório à sequência
        self.label_feedback.config(text="Memorize a sequência de números!")
        self.entry_resposta.delete(0, tk.END)  # Limpa o campo de resposta
        
        self.label_sequencia.config(text=" ".join(map(str, self.sequencia)))  # Exibe a sequência
        
        self.root.after(self.tempo_limite * 1000, self.limpar_sequencia)  # Após o tempo limite, limpa a sequência
        
    def limpar_sequencia(self):
        """ Função para esconder a sequência após o tempo """
        self.label_sequencia.config(text="")
        self.label_feedback.config(text="Digite a sequência de memória!")
        
        self.start_time = time.time()  # Marca o tempo de início para a resposta
        
    def checar_resposta(self):
        """ Função para verificar se a resposta está correta """
        resposta = self.entry_resposta.get().split()
        
        # Verifica se a resposta está correta
        if resposta == [str(num) for num in self.sequencia]:
            tempo_decorrido = time.time() - self.start_time
            self.pontuacao += 1
            self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}")
            self.label_rodada.config(text=f"Nível: {self.pontuacao + 1}")
            self.label_feedback.config(text=f"Resposta correta! Tempo: {int(tempo_decorrido)}s")
            self.root.after(1000, self.iniciar_nivel)  # Inicia o próximo nível
        else:
            self.label_feedback.config(text="Resposta incorreta! Jogo terminado.", fg="red")
            self.label_sequencia.config(text="")
            self.botao_enviar.config(state="disabled")  # Desabilita o botão após erro

# Função principal
def iniciar_jogo():
    root = tk.Tk()
    jogo = JogoMemoria(root)
    root.mainloop()

# Iniciar o jogo
iniciar_jogo()
