# Arquitetura do PulsoDigital API

Este documento descreve a arquitetura, padrões e práticas de desenvolvimento do projeto PulsoDigital API. É destinado a desenvolvedores e assistentes IA para garantir consistência e qualidade do código.

## Visão Geral da Arquitetura

O PulsoDigital API segue uma arquitetura em camadas baseada no padrão MCS (Model-Controller-Service) com Repository Pattern, proporcionando uma separação clara de responsabilidades e facilitando a manutenção.

## Estrutura de Pastas

```
/app
├── api
│   ├── dependencies.py    # Funções de injeção de dependências
│   └── routes/            # Endpoints da API (Controllers)
├── core
│   ├── bootstrap/         # Scripts de inicialização da aplicação
│   │   ├── db.py          # Configuração e inicialização do banco de dados
│   │   ├── seeder.py      # Classes para população inicial do banco
│   │   └── seeds/         # Seeds para dados iniciais
│   ├── models/            # Classes ORM SQLAlchemy
│   ├── schemas/           # Classes Pydantic para validação de dados
│   └── settings.py        # Configurações da aplicação
├── db
│   └── migrations/        # Migrações do banco de dados
├── repositories/          # Camada de acesso a dados
├── services/              # Camada de lógica de negócios
└── main.py                # Ponto de entrada da aplicação
```

## Fluxo de Trabalho Atualizado

1. **Rotas (Controllers)**:
   - Localizadas em `app/api/routes/`.
   - São responsáveis por receber requisições HTTP e delegar a lógica de negócio para os serviços.
   - Utilizam dependências injetadas para acessar os serviços.

2. **Serviços**:
   - Localizados em `app/services/`.
   - Implementam a lógica de negócio.
   - Utilizam repositórios para acessar os dados.
   - Convertem modelos ORM para schemas Pydantic para garantir consistência nas respostas.

3. **Repositórios**:
   - Localizados em `app/repositories/`.
   - Abstraem o acesso ao banco de dados.
   - Utilizam modelos ORM SQLAlchemy para realizar operações CRUD.

4. **Modelos (ORM)**:
   - Localizados em `app/core/models/`.
   - Representam as tabelas do banco de dados usando SQLAlchemy.

5. **Schemas (DTOs)**:
   - Localizados em `app/core/schemas/`.
   - Utilizam Pydantic para validação de dados e serialização/deserialização.
   - Configurados com `orm_mode = True` para permitir conversão de modelos ORM para schemas.

6. **Banco de Dados**:
   - Configurado em `app/core/bootstrap/db.py`.
   - Utiliza um singleton para gerenciar a conexão com o banco.
   - A função `get_db()` é usada para injetar sessões do banco de dados nas dependências.

7. **Seeder**:
   - Localizado em `app/core/bootstrap/seeder.py`.
   - Popula o banco de dados com dados iniciais (seeds).
   - Executado automaticamente no ambiente de desenvolvimento.

## Boas Práticas

- **Injeção de Dependências**:
  - Utilize o sistema de dependências do FastAPI para injetar serviços e repositórios.
  - Centralize as dependências em `app/api/dependencies.py`.

- **Validação de Dados**:
  - Utilize schemas Pydantic para validar dados de entrada e saída.
  - Configure `orm_mode = True` nos schemas para facilitar a conversão de modelos ORM.

- **Tratamento de Erros**:
  - Utilize `HTTPException` para erros HTTP.
  - Implemente validações específicas nos serviços para garantir consistência.

- **Transações de Banco de Dados**:
  - Gerencie transações no nível de repositório.
  - Utilize o método `commit()` apenas quando necessário.

- **Documentação**:
  - Documente funções e métodos com docstrings.
  - Mantenha este documento atualizado com mudanças arquiteturais.

## Fluxo de Execução

1. A requisição HTTP chega em uma rota (endpoint)
2. FastAPI valida os dados usando schemas Pydantic
3. A rota usa um serviço injetado via Depends()
4. O serviço implementa a lógica de negócio
5. O serviço usa um ou mais repositórios para acessar os dados
6. O repositório executa operações no banco de dados
7. Os dados retornam pela mesma cadeia
8. FastAPI serializa a resposta usando schemas

## Considerações para pgvector

- Para embeddings, mantenha as dimensões consistentes em toda a aplicação
- Use índices ANN (Approximate Nearest Neighbors) para consultas em larga escala:
  ```sql
  CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
  ```
- Otimize consultas limitando o número de resultados e usando filtros adicionais
- Para operações vetoriais complexas, considere usar SQL nativo

## Convenções de Código

- Use snake_case para nomes de arquivos, funções e variáveis
- Use PascalCase para nomes de classes (incluindo schemas e modelos)
- Prefixe schemas de criação com "Create", de atualização com "Update"
- Use anotações de tipo para todos os parâmetros e valores de retorno

Seguindo essas diretrizes, manteremos uma base de código consistente, testável e fácil de manter.