# 🤖 Automa_o_Manaus

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/github/license/Dinizgabri3l/Automa_o_Manaus)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Automação desenvolvida em Python utilizando Selenium e o navegador Microsoft Edge para execução de tarefas relacionadas à cidade de **Manaus**.

---

## 📂 Estrutura do Projeto

```
Automa_o_Manaus/
│
├── scripts/             # Scripts principais da automação
│   ├── main.py
│   ├── functions.py
│   └── transf.py
│
├── logs/                # Arquivos de log da execução
│
├── requirements.txt     # Dependências do projeto
├── msedgedriver.exe     # WebDriver para o Edge
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Como Executar

### 1. Pré-requisitos

- Python 3.9+ instalado
- Microsoft Edge instalado
- WebDriver (`msedgedriver.exe`) compatível com a versão do Edge

🔗 [Baixe o Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o script principal

```bash
python scripts/main.py
```

---

## 🕒 Execução automática (Agendador de Tarefas do Windows)

1. Abra o **Agendador de Tarefas** no Windows
2. Clique em **Criar Tarefa...**
3. Aba **Ações**:
   - Programa/script: `python`
   - Adicionar argumentos: `C:\caminho\para\Automa_o_Manaus\scripts\main.py`
   - Iniciar em: `C:\caminho\para\Automa_o_Manaus\`
4. Aba **Disparadores**:
   - Novo → Repetir a cada 12 horas
5. Marque “Executar com privilégios mais altos”
6. Salve a tarefa

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.9+](https://www.python.org/)
- [Selenium](https://selenium-python.readthedocs.io/)
- Microsoft Edge + msedgedriver

---

## ✅ Status do Projeto

O projeto está em desenvolvimento ativo. Melhorias, refatorações e testes estão sendo adicionados.

---

## 📑 Licença

Distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 🙌 Contribuições

Contribuições são bem-vindas!  
Sinta-se à vontade para abrir uma [Issue](https://github.com/Dinizgabri3l/Automa_o_Manaus/issues) ou enviar um Pull Request.

---

