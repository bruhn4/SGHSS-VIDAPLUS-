# SGHSS-VIDAPLUS-
## 📚 Sobre o projeto
Projeto acadêmico para a disciplina de Projetos: Desenvolvimento Back End  (Uninter). API back-end para gestão hospitalar, com cadastro de usuários, login, controle de consultas e segurança de dados.

## 🛠️ Ferramentas utilizadas 
* Python 3.11;
* Flask;
* Werkzeug;
* PyJWT;
* Insomnia.

## 🧱 Estrutura de diretórios 
<img width="287" height="381" alt="image" src="https://github.com/user-attachments/assets/f4ecfae5-6679-46f5-8d34-bd4a2ede6b95" />

## 🔎 Como rodar o projeto
1. Python 3.11 instalado na máquina;
2. IDE (ex:. VIsual Studio Code); 
3. Insomnia ou Postman para realizar os testes das rotas.

## 📩 Processo de instalação
1. Clone ou baixe os arquivos:
   * git clone https://github.com/seuusuario/SGHSS-VidaPlus.git
2. Acesse a pasta onde esta localizado o projeto:
   * cd  SGHSS-VidaPlus
3. Crie e ative o ambiente virtual:
   * python -m venv venv
   * venv\Scripts\activate (No windows)
4. Instale as dependências:
   * pip install flask werkzeug pyjwt
     
## 💻Executando o servidor 
- No terminal do VSCODE ou no cmd do POWERSHELL:
    * python app.py
- Se der tudo certo isto ira aparecer:
    * "Olá, servidor está funcionando!"

## 🔐 Endpoints
### Cadastro de Usuários
POST/usuarios 
Body (JSON)
{
  "nome": "Exemplo",
  "email": "exemplo@email.com",
  "senha": "123456",
  "perfil": "paciente"
}
### Login de usuário
POST/login
Body (JSON):
{
  "email": "exemplo@email.com",
  "senha": "123456"
}
### Edição de usuário
PUT/usuarios/<id>
Header: `Content-Type: application/json`
Body (JSON) 
{
  "nome": "Novo Nome",
  "senha": "novaSenha",
  "email": "novoemail@email.com"
}
 ## 👀 Observações:
 * Envie apenas os campos que deseja fazer alterações!
 * As senhas são criptografadas.
 * Informações com os seguintes dados: nome, email e senha são armazenadas em um arquivo json.
 * JWT é valido até 1h apartir do Login.

## 🪴Conclusão
Este é um projeto acadêmico que visa conceitos básicos de autenticação segurança dos dados e cosumo de APIs REST. 
