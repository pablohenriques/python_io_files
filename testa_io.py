arquivo = open("dados/contatos-escrita.csv", encoding="latin_1", mode="a+")
print(type(arquivo.buffer))
texto_em_bytes = bytes('Esse é um texto em bytes')
#print(f"Texto em bytes: {texto_em_bytes}")
#print(f"Tipo: {type(texto_em_bytes)}")
contato = bytes("15,Verônica,veronica@veronica.com.br\n", 'latin_1')
arquivo.buffer.write(contato)
arquivo.close()