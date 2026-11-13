import unittest
import os
import models
from app import app

class TestControleFinanceiro(unittest.TestCase):

    def setUp(self):
        self.test_db = "test_database.db"
        models.init_db(self.test_db)

        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    """Verifica se o banco de dados vai iniciar com as categorias."""
    def test_categorias_iniciais(self):
        conexao = models.sqlite3.connect(self.test_db)
        cursor = conexao.cursor()
        cursor.execute("select count(*) from categorias")
        total = cursor.fetchone()[0]
        conexao.close()
        self.assertEqual(total, 4)

    """Verifica a inserção e recuperação de uma transação."""
    def test_adicionar_e_listar_transacoes(self):
        models.add_transacoes("Salário", 5000.00, "2026-10-31", 1, db_name=self.test_db)
        transacoes = models.get_all_transacoes(db_name=self.test_db)

        self.assertEqual(len(transacoes), 1)
        self.assertEqual(transacoes[0]['descricao'], "Salário")
        self.assertEqual(transacoes[0]['valor'], 5000.00)
        self.assertEqual(transacoes[0]['tipo'], "receita")

    def test_rota_principal_status_200(self):
        """Testa a rota principal."""
        resposta = self.client.get('/')
        self.assertEqual(resposta.status_code, 200)

if __name__ == '__main__':
    unittest.main()
