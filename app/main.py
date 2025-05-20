from fastapi import FastAPI
import logging
from app.api.routes import theme, healthcheck, topic
from app.core.bootstrap.db import get_db_instance
from app.core.bootstrap.seeder import Seeder
from app.core.settings import settings

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PulsoDigital API",
    description="API para análise de dados e monitoramento de temas específicos",
    version="1.0.0"
)

# Registra as rotas
app.include_router(healthcheck.router)
app.include_router(theme.router)
app.include_router(topic.router)
#app.include_router(topic.router, prefix="/api/topics", tags=["Topics"])
#app.include_router(data_source.router, prefix="/api/data-sources", tags=["DataSources"])
#app.include_router(dashboard.router, prefix="/api/dashboards", tags=["Dashboards"])

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "Welcome to the PulsoDigital API!"}

# Inicializa o banco de dados e seeds na inicialização
@app.on_event("startup")
async def startup():
    logger.info("Inicializando aplicação...")

    # Inicializa o banco de dados
    db = get_db_instance()
    
    # Verifica a conexão com o banco
    if not db.verify_connection(max_retries=15, base_delay=2, max_delay=30):
        logger.error("Não foi possível conectar ao banco de dados")
        raise Exception("Não foi possível conectar ao banco de dados")
    
    # Cria as tabelas se não existirem
    try:
        db.create_tables()
        logger.info("Tabelas verificadas/criadas com sucesso")
    except Exception as e:
        logger.error("Erro ao criar tabelas: %s", str(e))
        raise
    
    # Executa os seeds se estiver em ambiente de desenvolvimento
    environment = getattr(settings, "ENVIRONMENT", "development")
    if environment.lower() == "development":
        logger.info("Ambiente de desenvolvimento detectado. Executando seeds...")
        seeder = Seeder(db)
        try:
            seeder.run_all_seeds()
            logger.info("Seeds executados com sucesso")
        except Exception as e:
            logger.error("Erro ao executar seeds: %s", str(e))
    
    logger.info("Aplicação inicializada com sucesso")

@app.on_event("shutdown")
async def shutdown():
    logger.info("Encerrando aplicação...")
    # Aqui podemos adicionar lógica de limpeza se necessário