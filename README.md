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

import openpyxl

# 1. Abre a planilha
arquivo = openpyxl.load_workbook('Planilha_Funcionarios.xlsx')
aba = arquivo.active

# 2. Escreve o cabeçalho da coluna D
aba["D1"] = "Salario Liquido"

# 3. Mostra no terminal
print("======== FUNCIONÁRIOS DA EMPRESA ========")
total_salarios = 0
quantidade = 0

# 4. Percorre cada funcionário
for linha in aba.iter_rows(min_row=2, values_only=False):
    #                                          ↑ False porque vamos ESCREVER

    nome    = linha[0].value  # coluna A
    salario = linha[1].value  # coluna B
    cargo   = linha[2].value  # coluna C

    # 5. Calcula o salário líquido (desconto de 18.5%)
    salario_liquido = salario * 0.815

    # 6. Escreve o resultado na coluna D da planilha
    linha[3].value = salario_liquido

    # 7. Mostra no terminal
    print(f"{cargo:<15} | {nome:<20} | R${salario:.2f} | Liq: R${salario_liquido:.2f}")

    total_salarios += salario
    quantidade += 1

# 8. Resumo no terminal
print("==========================================")
print(f"Total de funcionários: {quantidade}")
print(f"Total de salários:     R${total_salarios:.2f}")
print(f"Média salarial:        R${total_salarios / quantidade:.2f}")
print("==========================================")

# 9. Salva a planilha com a nova coluna
arquivo.save("Planilha_Funcionarios.xlsx")
print("Planilha atualizada com salários líquidos!")

## 👨‍💻 Autor

Marcos Levy — Estudante de Ciência da Computação | Foco em Cibersegurança
