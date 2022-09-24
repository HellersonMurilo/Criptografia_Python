#teste criptografia 03

import string
import random
from getpass import getpass

chave = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 1024))

senha = input("Digite a senha desejada para dar continuidade a criptografia: ")

mensagem = getpass('Digite a mensagem secreta: ')

def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1,s2)])



secreta = str_xor(mensagem, chave)

print("Mensagem secreta: "+secreta + "\n")

recuperando_mensagem_secreta = input("Digite a senha: ")
if recuperando_mensagem_secreta == senha:
  print("Mensagem descriptografada: " + "\n" + mensagem + "\n")
else: 
  print("Senha para descriptografia incorreta!")