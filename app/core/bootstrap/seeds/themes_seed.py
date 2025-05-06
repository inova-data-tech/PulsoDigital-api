from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.core.models.theme import Theme
import logging

logger = logging.getLogger(__name__)

def run(session: Session):
    """
    Popula a tabela themes com dados iniciais.
    
    Args:
        session (Session): Uma sessão de banco de dados SQLAlchemy
    """
    # Lista de temas a serem inseridos
    themes = [
        {"name": "Economia"},
        {"name": "Política"},
        {"name": "Saúde"},
        {"name": "Educação"},
        {"name": "Tecnologia"},
        {"name": "Meio Ambiente"},
        {"name": "Segurança"},
        {"name": "Cultura"},
        {"name": "Esportes"},
        {"name": "Ciência"}
    ]
    
    # Verifica se já existem registros para evitar duplicação
    existing_count = session.query(Theme).count()
    
    if existing_count == 0:
        logger.info("Inserindo temas iniciais no banco de dados")
        for theme_data in themes:
            try:
                theme = Theme(**theme_data)
                session.add(theme)
                # Commit após cada inserção para evitar problemas com nomes duplicados
                session.commit()
                logger.debug("Tema '%s' inserido com sucesso", theme_data["name"])
            except IntegrityError:
                # Se houver erro de integridade (ex: nome duplicado), faça rollback e continue
                session.rollback()
                logger.warning("Tema '%s' já existe, ignorando", theme_data["name"])
            except Exception as e:
                session.rollback()
                logger.error("Erro ao inserir tema '%s': %s", theme_data["name"], str(e))
        
        logger.info("Seed de temas concluído")
    else:
        logger.info("Tabela de temas já possui registros. Seed ignorado.")