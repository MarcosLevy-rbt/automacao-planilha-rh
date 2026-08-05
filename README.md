# automacao-planilha-rh
Automação em Python para leitura e análise de planilhas de funcionários com openpyxl

# 📊 Automação de Planilha de RH

Automação desenvolvida em Python para leitura e análise de planilhas de funcionários de uma empresa.

## 💡 O que esse projeto faz?

- Lê automaticamente uma planilha Excel com dados de funcionários
- Exibe nome, departamento, cargo, salário, cidade e status de cada um
- Calcula o total de salários da empresa
- Conta quantos funcionários estão **ativos** e **inativos**

## 🛠️ Tecnologias usadas

- Python 3
- openpyxl

## 📁 Estrutura esperada da planilha

| ID | Nome | Departamento | Cargo | Salário | Admissão | Cidade | Status |
|----|------|--------------|-------|---------|----------|--------|--------|
| 1  | Ana Silva | RH | Analista | 3500 | 01/01/2022 | Brasília | Ativo |

## ▶️ Como executar

1. Instale a dependência:
```bash
pip install openpyxl
```

2. Coloque sua planilha `funcionarios.xlsx` na mesma pasta

3. Execute:
```bash
python automacao.py
```

## 📌 Exemplo de saída

```
=============== FUNCIONÁRIOS DA EMPRESA ===============
Nome: Ana Silva | Depto: RH | Cargo: Analista | Salário: R$ 3500.00 | Status: Ativo
=======================================================
Salário total da empresa: R$ 12400.00
Quantidade de funcionários: 4
Funcionários ativos: 3
Funcionários inativos: 1
=======================================================
```

## 👨‍💻 Autor

Marcos Levy — Estudante de Ciência da Computação | Foco em Cibersegurança
