# Changelog - 2025-05-06

## Changes since db66c4308d5451228077cd5cfa55c00a621a8551

### Features
* feat: adicionar workflow para geração automática de changelog
* feat: adicionar configuração de logging e inicialização do banco de dados na aplicação
* feat: adicionar dependências para repositórios e serviços de tema
* feat: implementar CRUD para temas com serviços e repositórios
* feat: adicionar arquivos de  migrações para o banco de dados
* feat: adicionar seeder para popular a tabela de temas com dados iniciais
* feat: adicionar configuração de settings para gerenciamento de variáveis de ambiente e conexão com o banco de dados
* feat: implementar gerenciamento de conexão com o banco de dados e remover sessão antiga

### Bug Fixes


### Documentation
* docs: adicionar regras para commits seguindo a convenção Conventional Commits
* docs: Adicionar documentos de changelogs e arquitetura do projeto

### Performance Improvements


### Refactoring
* refactor: ajustar rota do healthcheck para simplificar a URL e melhorar a legibilidade
* refactor: atualizar importações do Base para o novo caminho no bootstrap
* refactor: remover arquivo de configurações de ambiente desnecessário
* refactor: Reorganizar instruções de cópia no Dockerfile para melhorar a instalação de dependências
* refactor: Atualizar arquivo .env.example para remover configurações obsoletas e organizar variáveis de ambiente

### Other Changes
* ci(implement auto changelogs): :memo: Adicionar arquivo de configuração do GitHub Actions para CI

