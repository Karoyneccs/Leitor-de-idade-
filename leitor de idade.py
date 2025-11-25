dias_totais = int(input("Digite sua idade em dias: "))

anos = dias_totais // 365
resto = dias_totais % 365

meses = resto // 30
dias = resto % 30

print(f"{anos} ano(s), {meses} mes(es) e {dias} dia(s)")
