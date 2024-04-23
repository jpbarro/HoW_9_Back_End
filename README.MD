### Criar Usuario
- **Endpoint:** `POST /users/create_user/`
  - **Descrição:** Cria um user novo na database.
- **Corpo da Requisição:**
  - `username` (string, obrigatório): Nome de usuário.
  - `password` (string, obrigatório): Senha do usuário.
  - `email` (string, opcional): Email do usuário (pode ser usado para recuperação de senha).
- **Resposta de Sucesso:**
  - `user_id` (int): ID único do usuario criado
- **Resposta de Erro:**
  - 400 Bad Request: Dados de entrada inválidos.
  - 401 Unauthorized: Credenciais inválidas.

### Gerar Token de Acesso

- **Endpoint:** `POST /api/token/`
- **Descrição:** Gera um token de acesso JWT para autenticação.
- **Corpo da Requisição:**
  - `username` (string, obrigatório): Nome de usuário.
  - `password` (string, obrigatório): Senha do usuário.
  - `email` (string, opcional): Email do usuário (pode ser usado para recuperação de senha).
- **Resposta de Sucesso:**
  - `access` (string): Token de acesso JWT válido por um período de tempo.
  - `refresh` (string): Token de acesso JWT válido por um período de tempo.
- **Resposta de Erro:**
  - 400 Bad Request: Dados de entrada inválidos.
  - 401 Unauthorized: Credenciais inválidas.

### Criar um Post

- **Endpoint:** `POST /posts/`
- **Descrição:** Cria um novo post.
- **Cabeçalho da Requisição:**
  - `Authorization` (string, obrigatório): Acess Token gerado no endpoint `/api/token/`.
- **Corpo da Requisição:**
  - `title` (string, obrigatório): Título do post.
  - `content` (string, obrigatório): Conteúdo do post.
- **Resposta de Sucesso:**
  - `id` (int): ID único do post criado.
  - `title` (string): Título do post.
  - `content` (string): Conteúdo do post.
  - `author` (int): ID único do usuario que criou post.
  - `created_at` (string): Data da criação.
  - `updated_at` (string): Data do update.
- **Resposta de Erro:**
  - 400 Bad Request: Dados de entrada inválidos.
  - 401 Unauthorized: Token de acesso inválido ou expirado.

### Deletar um Post

- **Endpoint:** `DELETE /posts/{id}/`
- **Descrição:** Deleta um post.
- **Cabeçalho da Requisição:**
  - `Authorization` (string, obrigatório): Acess Token gerado no endpoint `/api/token/`.
- **Corpo da Requisição:**
  - Não é necessario, autenticação realizada pelo token.
- **Resposta de Sucesso:**
  - "message": "Post '{title}' deletado com sucesso."
- **Resposta de Erro:**
  - 404: Post não encontrado.
  - 401 Unauthorized: Token de acesso inválido ou expirado.
  - 500: Erro ao deletar o post

### Obter Todos os Posts

- **Endpoint:** `GET /posts/`
- **Descrição:** Retorna todos os posts.
- **Cabeçalho da Requisição:**
  - `Authorization` (string, obrigatório): Acess Token gerado no endpoint `/api/token/`.
- **Resposta de Sucesso:**
  - Lista de objetos de post, cada um contendo:
    - `id` (int): ID único do post.
    - `title` (string): Título do post.
    - `content` (string): Conteúdo do post.
    - `author` (int): ID único do usuario que criou post.
    - `created_at` (string): Data da criação.
    - `updated_at` (string): Data do update.
- **Resposta de Erro:**
  - 401 Unauthorized: Token de acesso inválido ou expirado.