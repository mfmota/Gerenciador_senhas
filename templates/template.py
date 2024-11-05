import sys,os
sys.path.append(os.path.abspath(os.curdir))

from model.password import Password
from views.password_views import FernetHasher


action = input('Digite \n 1-Salvar nova senha \n 2-Ver senha salva\n')

match action:
    case '1':
        if len(Password.get()) == 0:
            key, path = FernetHasher.create_key(archive=True)
            print ('Chave criada!')
            print(f'{key.decode("utf-8")}')
            if path:
                print('Chave salva no arquivo')
                print(f'Caminho: {path}')
        else:
            key = input('Digite a chave usa para criptografia')    
            
        domain = input('Dominio: ')
        password = input('Senha: ')
        fernet_user = FernetHasher(key)
        p1 = Password(domain=domain,password=fernet_user.encrypt(password).decode('utf-8'))
        p1.save()

    case '2':
        domain = input("Dominio: ")
        key = input('key: ')
        fernet_user = FernetHasher(key)
        data = Password.get()
        for i in data:
            if domain in i['domain']:
                password = fernet_user.decrypt(i['password'])
        if password:
            print(f'Sua senha: {password}')
        else: 
            print('Nenhuma senha encotrada para o dominio')            