import customtkinter as ctk
import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

MOEDAS = ['USD', 'BRL', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']

def buscar_taxa(base, destino):
    ''' Busca a taxa de conversão entre duas moedas usando a API FreeCurrencyAPI. '''
    API_KEY = os.getenv('API_KEY')
    url = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&base_currency={base}&currencies={destino}'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        return dados['data'][destino]
    except Exception as e:
        print(f"Erro ao buscar taxa: {e}")
        return None

def mostrar_resultado(mensagem):
    ''' Cria uma janela de resultado com a mensagem fornecida. '''
    resultado = ctk.CTkToplevel(janela)
    resultado.title("Resultado")
    resultado.geometry("500x200")
    resultado.configure(fg_color='#3b5f41')
    resultado.resizable(False, False)
    resultado.lift()
    resultado.focus_force()
    resultado.attributes('-topmost', True)
    resultado.after(200, lambda: resultado.attributes('-topmost', False))
    fonte_resultado = ("Courier", 20, "bold")
    ctk.CTkLabel(
        resultado,
        text=mensagem,
        bg_color='#3b5f41',
        text_color='white',
        font=fonte_resultado,
        justify='center'
    ).pack(expand=True, fill='both', padx=20, pady=20)
    ctk.CTkButton(
        resultado,
        text="OK",
        command=resultado.destroy,
        font=("Courier", 16, "bold"),
        fg_color='#c94f4f',
        text_color='white',
        hover_color='#a03c3c',
        corner_radius=15,
        width=80,
        height=35
    ).pack(pady=(0, 15))

    # Centralizar a janela de resultado na tela
    resultado.update_idletasks()
    largura = 500
    altura = 200
    largura_tela = resultado.winfo_screenwidth()
    altura_tela = resultado.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    resultado.geometry(f"{largura}x{altura}+{x}+{y}")

def converter_valor():
    ''' Converte o valor informado de uma moeda para outra. '''
    try:
        valor = float(valor_var.get())
        moeda_origem = moeda_origem_var.get()
        moeda_destino = moeda_destino_var.get()
        if moeda_origem == moeda_destino:
            mostrar_resultado(f"O valor convertido é o mesmo: {valor:.2f} {moeda_destino}")
            return
        taxa = buscar_taxa(moeda_origem, moeda_destino)
        if taxa is None:
            mostrar_resultado("Não foi possível obter a taxa de conversão.")
            return
        valor_convertido = valor * taxa
        mensagem = (
            f"{valor:.2f} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}\n"
            f"Taxa de conversão: 1.00 {moeda_origem} = {taxa:.2f} {moeda_destino}"
        )
        mostrar_resultado(mensagem)
    except ValueError:
        mostrar_resultado("Digite um valor numérico válido.")

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Interface CustomTkinter
janela = ctk.CTk(fg_color='#3b5f41')
janela.title("Conversor de Moedas")
largura = 900
altura = 600
janela.geometry(f"{largura}x{altura}")
janela.resizable(False, False)

# Centralizar a janela
janela.update_idletasks()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Fontes
fonte_titulo = ("Courier", 40)
fonte_label = ("Courier", 22)
fonte_botao = ("Courier", 20, "bold")

# Título centralizado
ctk.CTkLabel(
    janela,
    text="CONVERSOR DE MOEDAS",
    font=fonte_titulo,
    text_color='white',
    bg_color='#3b5f41'
).place(relx=0.5, y=80, anchor="center")

# Valor
ctk.CTkLabel(
    janela, text="Valor:", font=fonte_label, text_color='white', bg_color='#3b5f41'
).place(x=120, y=220)
valor_var = ctk.StringVar()
ctk.CTkEntry(
    janela, textvariable=valor_var, font=fonte_label, fg_color='white', text_color='#000000',
    border_width=0, corner_radius=15, width=200, height=45
).place(x=220, y=215)

# Moeda de origem
ctk.CTkLabel(
    janela, text="Moeda:", font=fonte_label, text_color='white', bg_color='#3b5f41'
).place(x=500, y=220)
moeda_origem_var = ctk.StringVar(value=MOEDAS[0])
ctk.CTkComboBox(
    janela, variable=moeda_origem_var, values=MOEDAS, font=fonte_label, fg_color='white',
    text_color='#000000', border_width=0, corner_radius=15, width=150, height=45
).place(x=610, y=215)

# Converter para
ctk.CTkLabel(
    janela, text="Converter para:", font=fonte_label, text_color='white', bg_color='#3b5f41'
).place(x=210, y=320)
moeda_destino_var = ctk.StringVar(value=MOEDAS[1])
ctk.CTkComboBox(
    janela, variable=moeda_destino_var, values=MOEDAS, font=fonte_label, fg_color='white',
    text_color='#000000', border_width=0, corner_radius=15, width=150, height=45
).place(x=450, y=315)

# Botão calcular
ctk.CTkButton(
    janela,
    text="CALCULAR",
    command=converter_valor,
    font=fonte_botao,
    fg_color='#c94f4f',
    text_color='white',
    hover_color='#a03c3c',
    corner_radius=25,
    width=180,
    height=55
).place(relx=0.5, y=430, anchor="center")

janela.mainloop()