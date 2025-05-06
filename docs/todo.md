# TODO

## Concluído

- [x] Implementar classe `DB` para gerenciar conexões e criar tabelas.
- [x] Implementar função `get_db()` para injeção de dependências.
- [x] Criar classe `Seeder` para popular o banco de dados com dados iniciais.
- [x] Criar seed para a entidade `Theme`.
- [x] Implementar repositório para a entidade `Theme`.
- [x] Implementar serviço para a entidade `Theme`.
- [x] Implementar rotas para a entidade `Theme`.
- [x] Corrigir erro de confusão entre schemas Pydantic e modelos ORM.
- [x] Adicionar lógica de reconexão ao banco de dados com backoff exponencial.

## Pendências

### Dashboard
- [ ] Criar modelo ORM para `Dashboard`.
- [ ] Criar schema Pydantic para `Dashboard`.
- [ ] Implementar repositório para `Dashboard`.
- [ ] Implementar serviço para `Dashboard`.
- [ ] Implementar rotas para `Dashboard`.

### Data Source
- [ ] Criar modelo ORM para `DataSource`.
- [ ] Criar schema Pydantic para `DataSource`.
- [ ] Implementar repositório para `DataSource`.
- [ ] Implementar serviço para `DataSource`.
- [ ] Implementar rotas para `DataSource`.

### Topic
- [ ] Criar modelo ORM para `Topic`.
- [ ] Criar schema Pydantic para `Topic`.
- [ ] Implementar repositório para `Topic`.
- [ ] Implementar serviço para `Topic`.
- [ ] Implementar rotas para `Topic`.

## Melhorias Futuras

- [ ] Adicionar testes unitários para repositórios, serviços e rotas.
- [ ] Melhorar logs para rastreamento de erros.
- [ ] Adicionar suporte a migrações de banco de dados com Alembic.
- [ ] Implementação de celery para processos de rotina de scrap de informações
- [ ] Implementação de redis para cache de informações