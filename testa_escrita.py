arquivos_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a+')

contatos = [
    '11,Carol,carol@carol.com.br\n',
    '12,Ana,ana@ana.com.br\n',
    '13,Tais,tais@tais.com.br\n',
    '14,Felipe,felipe@felipe.com.br\n',
]

for contato in contatos:
    arquivos_contatos.write(contato)

arquivos_contatos.flush()
arquivos_contatos.seek(28)
arquivos_contatos.write('12,Ana,ana@ana.com.br\n'.upper())
arquivos_contatos.flush()
arquivos_contatos.seek(0)

for linha in arquivos_contatos:
    print(linha)

