from pathlib import Path
import importlib
import logging
from sqlalchemy.orm import Session
from app.core.bootstrap.db import DB

logger = logging.getLogger(__name__)

class Seeder:
    """
    Classe responsável por popular o banco de dados com dados iniciais (seeds).
    Utiliza os arquivos de seed no diretório seeds.
    """
    def __init__(self, db: DB):
        """
        Inicializa o Seeder com uma instância de DB.
        
        Args:
            db (DB): Uma instância da classe DB para acesso ao banco
        """
        self.db = db
        self.seeds_dir = Path(__file__).parent / "seeds"
        if not self.seeds_dir.exists():
            logger.warning("Diretório de seeds não encontrado: %s", str(self.seeds_dir))
            self.seeds_dir.mkdir(parents=True, exist_ok=True)
    
    def run_all_seeds(self):
        """
        Executa todos os seeds disponíveis no diretório seeds.
        Os seeds são identificados pelo padrão *_seed.py
        """
        logger.info("Iniciando execução de todos os seeds...")
        
        try:
            seed_files = list(self.seeds_dir.glob("*_seed.py"))
            if not seed_files:
                logger.warning("Nenhum arquivo de seed encontrado em: %s", str(self.seeds_dir))
                return
            
            logger.info("Encontrados %d arquivos de seed", len(seed_files))
            
            # Obter uma sessão do banco de dados
            session = next(self.db.get_session())
            
            for seed_file in seed_files:
                seed_name = seed_file.stem  # Nome do arquivo sem extensão
                logger.info("Executando seed: %s", seed_name)
                
                try:
                    module_name = f"app.core.bootstrap.seeds.{seed_name}"
                    seed_module = importlib.import_module(module_name)
                    
                    # Executa a função run do módulo de seed
                    seed_module.run(session)
                    logger.info("Seed %s executado com sucesso", seed_name)
                except Exception as e:
                    logger.error("Erro ao executar seed %s: %s", seed_name, str(e))
                    session.rollback()  # Garantir rollback em caso de erro
            
            logger.info("Todos os seeds foram processados")
        except Exception as e:
            logger.error("Erro ao executar seeds: %s", str(e))
    
    def run_seed(self, seed_name: str):
        """
        Executa um seed específico pelo nome.
        
        Args:
            seed_name (str): Nome do seed (sem o sufixo _seed.py)
        """
        try:
            full_seed_name = f"{seed_name}_seed"
            logger.info("Executando seed específico: %s", full_seed_name)
            
            # Verifica se o arquivo de seed existe
            seed_path = self.seeds_dir / f"{full_seed_name}.py"
            if not seed_path.exists():
                logger.error("Arquivo de seed não encontrado: %s", str(seed_path))
                return
            
            # Importa e executa o seed
            module_name = f"app.core.bootstrap.seeds.{full_seed_name}"
            seed_module = importlib.import_module(module_name)
            
            # Obtenha uma sessão do pool
            with self.db.SessionLocal() as session:
                seed_module.run(session)
            
            logger.info("Seed %s executado com sucesso", full_seed_name)
        except Exception as e:
            logger.error("Erro ao executar seed %s: %s", seed_name, str(e))
            raise