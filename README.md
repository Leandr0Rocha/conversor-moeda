# Conversor de Moedas

![image](https://github.com/user-attachments/assets/f1db2799-e4a3-4eb4-9aea-d1556038d3ea)

Uma aplicação gráfica simples para conversão de moedas, desenvolvida em Python utilizando [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) para uma interface moderna e estilizada.

## Funcionalidades

- Conversão entre diversas moedas internacionais.
- Interface amigável e responsiva.
- Exibição da taxa de conversão utilizada.
- Caixa de entrada e seleção com cantos arredondados.

![image](https://github.com/user-attachments/assets/b8ab7c1f-aaef-4f7d-8f79-a89fa6bbc25d)

## Como usar

1. **Clone o repositório** e acesse a pasta do projeto.
2. **Instale as dependências**:
   ```
   pip install -r requirements.txt
   ```
3. **Execute o aplicativo**:
   ```
   python app.py
   ```

## Configuração da chave da API

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
API_KEY=sua_chave_aqui
```

Substitua `sua_chave_aqui` pela sua chave da Free Currency API. Para gerar uma chave é necessário se cadastrar no site da API.

## API utilizada

- [Free Currency API](https://freecurrencyapi.com/)

A Free Currency API foi utilizada para obter as taxas de câmbio em tempo real entre as moedas selecionadas. O projeto faz uma requisição HTTP para a API sempre que o usuário solicita uma conversão, garantindo que os valores estejam sempre atualizados. O uso da API proporcionou aprendizado prático sobre como consumir serviços externos em Python, lidar com requisições HTTP, tratamento de respostas JSON e gerenciamento de possíveis erros de conexão ou dados.

## Interface gráfica

A interface foi construída com CustomTkinter, uma extensão moderna do Tkinter que permite criar componentes visuais mais bonitos e personalizáveis, como caixas de entrada e botões com cantos arredondados e cores customizadas. O desenvolvimento da interface gráfica proporcionou experiência com posicionamento absoluto e relativo de widgets, manipulação de eventos (como cliques de botões), centralização de janelas e aplicação de estilos para melhorar a experiência do usuário.

## Vídeo utilizado como base

- [YouTube: Conversor de Moedas (em inglês)](https://youtu.be/zT7niRUOs9o?si=7joc0xuNQ4b_BPH9)

---

## Aprendizados

Ao realizar este projeto, foi possível aprofundar conhecimentos em:

- Consumo de APIs REST em Python.
- Manipulação de dados JSON.
- Tratamento de exceções e mensagens de erro para o usuário.
- Criação de interfaces gráficas modernas e responsivas com CustomTkinter.
- Organização do código em funções reutilizáveis e separação de responsabilidades.
- Melhoria da experiência do usuário com feedback visual e centralização de janelas.

Este projeto é uma ótima base para quem deseja aprender integração entre Python, APIs externas e interfaces gráficas, além de boas práticas de usabilidade.
