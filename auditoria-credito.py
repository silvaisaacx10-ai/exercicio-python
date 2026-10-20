# Sistema de Auditoria de Crédito - ArkeTech

print("=== SISTEMA DE AUDITORIA DE CRÉDITO ARKETECH ===")

# 1. Coleta de dados do solicitante
nome_empresa = input("Digite o nome da empresa solicitante: ")
faturamento_mensal = float(input("Digite o faturamento mensal (R$): "))
valor_emprestimo = float(input("Digite o valor do empréstimo solicitado (R$): "))

# 2. Processamento do cálculo (empréstimo dividido em 12 vezes sem juros)
parcela_mensal = valor_emprestimo / 12

# 3. Árvore de decisão baseada no risco
if parcela_mensal <= (faturamento_mensal * 0.30):
    status = "APROVADO"
elif parcela_mensal <= (faturamento_mensal * 0.50):
    status = "EM ANÁLISE (Risco Moderado)"
else:
    status = "RECUSADO"

# 4. Exibição da saída formatada utilizando f-strings
print("\n" + "="*40)
print(f"RELATÓRIO DE AUDITORIA: {nome_empresa}")
print("="*40)
print(f"Faturamento Mensal: R$ {faturamento_mensal:,.2f}")
print(f"Valor do Empréstimo: R$ {valor_emprestimo:,.2f}")
print(f"Parcela Mensal (12x): R$ {parcela_mensal:,.2f}")
print(f"Parecer Final: {status}")
print("="*40)