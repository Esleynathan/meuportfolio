import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Aguardando o banco de dados...")
        db_conn = None
        attempts = 0
        while not db_conn and attempts < 30:  # Tenta por 30 segundos
            try:
                db_conn = connections['default']
                db_conn.cursor()  # Tenta obter um cursor para forçar a conexão
            except OperationalError:
                self.stdout.write("Banco de dados indisponível, aguardando 1 segundo...")
                time.sleep(1)
                attempts += 1

        if db_conn:
            self.stdout.write(self.style.SUCCESS('Banco de dados disponível!'))
        else:
            self.stdout.write(self.style.ERROR('Não foi possível conectar ao banco de dados após 30 segundos.'))
            exit(1)

