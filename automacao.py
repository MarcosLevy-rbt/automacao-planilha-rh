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
