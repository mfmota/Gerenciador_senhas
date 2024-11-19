# Password Manager

Este projeto é um sistema de gerenciamento de senhas, que usa o módulo `cryptography.fernet` para criptografar e armazenar senhas de forma segura. Ele permite que o usuário crie e armazene senhas criptografadas, além de recuperá-las utilizando uma chave de criptografia previamente gerada.

## Estrutura do Projeto

O projeto contém três módulos principais:

1. **password_views.py**: Define a classe `FernetHasher` para gerar, arquivar e gerenciar chaves, além de fornecer métodos para criptografar e descriptografar senhas.
2. **template.py**: Script principal que interage com o usuário e executa ações de salvar e recuperar senhas, utilizando `FernetHasher` e `Password`.
3. **password.py**: Define a classe `Password`, que herda de `BaseModel`, para modelar e armazenar as senhas em um arquivo de texto.

## Requisitos

- Python 3.x
- Módulo `cryptography` (`pip install cryptography`)

## Configuração

1. Clone este repositório.
   $ git clone https://github.com/mfmota/Gerenciador_senhas.git
2. Instale os requisitos com o comando:
   ```bash
   pip install cryptography
## Uso
    ```bash
python template/template.py

## Exemplos de uso

### Salvando uma nova senha
```plaintext
Digite 
1-Salvar nova senha
2-Ver senha salva
> 1
Chave criada!
<Chave>
Dominio: example.com
Senha: senha_secreta
```
### Recuperando a senha
```plaintext
Digite 
1-Salvar nova senha
2-Ver senha salva
> 2
Dominio: example.com
Chave: <Chave>
Sua senha: senha_secreta
```

##Licença
Esse README cobre todos os pontos principais, incluindo a estrutura, uso e explicações detalhadas sobre os módulos e classes do projeto.


