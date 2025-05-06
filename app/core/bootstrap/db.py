from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy.pool import QueuePool
from app.core.settings import settings
import logging
import time
import random

logger = logging.getLogger(__name__)

# Criando a Base para os modelos SQLAlchemy
Base = declarative_base()

# Instância global do DB (singleton)
_db_instance = None

class DB:
    """
    Classe responsável pela configuração e gerenciamento da conexão com o banco de dados.
    Implementa métodos para verificar conexão, criar tabelas e gerenciar o pool de conexões.
    """
    def __init__(self):
        """
        Inicializa a conexão com o banco de dados usando as configurações do settings.
        Configura o pool de conexões e sessões.
        """
        self.engine = create_engine(
            settings.DATABASE_URL,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=1800
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        logger.info("DB engine inicializado com URL: %s", settings.DATABASE_URL)
    
    def create_tables(self):
        """
        Cria todas as tabelas definidas nos modelos SQLAlchemy.
        As tabelas são criadas apenas se ainda não existirem.
        """
        try:
            logger.info("Criando tabelas no banco de dados...")
            Base.metadata.create_all(bind=self.engine)
            logger.info("Tabelas criadas com sucesso")
            return True
        except Exception as e:
            logger.error("Erro ao criar tabelas: %s", str(e))
            raise
    
    def verify_connection(self, max_retries=10, base_delay=1, max_delay=30):
        """
        Verifica se a conexão com o banco de dados está funcionando.
        Implementa uma estratégia de tentativas múltiplas com backoff exponencial
        para dar tempo ao banco de dados para iniciar completamente.
        
        Args:
            max_retries (int): Número máximo de tentativas de reconexão
            base_delay (int): Tempo de espera base entre tentativas (em segundos)
            max_delay (int): Tempo máximo de espera entre tentativas (em segundos)
        
        Returns:
            bool: True se a conexão for estabelecida com sucesso, False após todas as tentativas falharem
        """
        attempt = 0
        
        while attempt < max_retries:
            try:
                with self.engine.connect() as conn:
                    conn.execute(text("SELECT 1"))
                    logger.info("Conexão com o banco de dados verificada com sucesso na tentativa %d", attempt + 1)
                    return True
            except Exception as e:
                attempt += 1
                
                if attempt >= max_retries:
                    logger.error("Falha ao verificar conexão após %d tentativas. Último erro: %s", 
                                max_retries, str(e))
                    return False
                
                # Backoff exponencial com jitter para evitar tempestade de reconexões
                delay = min(base_delay * (2 ** (attempt - 1)) + random.uniform(0, 1), max_delay)
                
                logger.warning("Falha na tentativa %d de conexão com o banco: %s. Tentando novamente em %.2f segundos...", 
                              attempt, str(e), delay)
                
                # Aguarda antes da próxima tentativa
                time.sleep(delay)
        
        # Isso só deveria ser alcançado se max_retries for <= 0
        return False
    
    def get_session(self):
        """
        Retorna uma sessão do pool de conexões.
        Este método deve ser usado como um gerador em um contexto.
        
        Yields:
            Session: Uma sessão de banco de dados
        """
        db = self.SessionLocal()
        try:
            logger.debug("Sessão de banco de dados criada")
            yield db
        finally:
            logger.debug("Sessão de banco de dados fechada")
            db.close()

# Função para obter a instância única de DB
def get_db_instance():
    global _db_instance
    if _db_instance is None:
        _db_instance = DB()
    return _db_instance

# Modificar esta função
def get_db():
    """
    Função que retorna uma sessão do banco de dados.
    Para usar com o sistema de dependência do FastAPI.
    
    Returns:
        Session: Uma sessão SQLAlchemy
    """
    db = get_db_instance().SessionLocal()
    try:
        yield db
    finally:
        db.close()