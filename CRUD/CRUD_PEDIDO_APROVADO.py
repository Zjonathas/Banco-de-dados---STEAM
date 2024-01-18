import mysql.connector as connector
from datetime import datetime


class DataBase:
    @staticmethod
    def connect():
        """Realiza a conexão com o database da steam"""
        try:
            connetion = connector.connect(
                host="",
                user="",
                password="",
                database=""
            )
            return connetion
        except connector.Error as erro:
            print(f"Erro ao conectar: {erro.msg}")


class CrudVisitRequest:
    def __init__(self):
        self.database = DataBase()
        self.connection = None
        self.cursor = None

    def insert_visit_accept(self, id_pedido, nome_aprovador):
        command = ("INSERT INTO pedidos_aprovados (id_pedido, data_aprovacao, nome_aprovador) VALUES "
                   "(%s, %s, %s)")
        date = datetime.now()
        value = (id_pedido, date, nome_aprovador)

        self.execute_and_close(command, value)

    def search_visit_id_accept(self, cod_aprovado):
        connection = self.database.connect()
        cursor = connection.cursor()

        command = "SELECT * FROM pedidos_aprovados WHERE id_pedido = %s"
        value = (cod_aprovado,)

        cursor.execute(command, value)

        result = cursor.fetchall()
        print(result)

        cursor.close()
        connection.close()
        return result

    def search_visit_cod_accept(self, cod_aprovado):
        connection = self.database.connect()
        cursor = connection.cursor()

        command = "SELECT * FROM pedidos_aprovados WHERE cod_aprovado = %s"
        value = (cod_aprovado,)

        cursor.execute(command, value)

        result = cursor.fetchall()
        print(result)

        cursor.close()
        connection.close()
        return result

    def search_visit_accept(self, nome_visitante):
        connection = self.database.connect()
        cursor = connection.cursor()

        command = """SELECT * FROM pedidos_aprovados NATURAL JOIN pedido_de_visita
                   WHERE nome_visitante LIKE %s"""

        value = (nome_visitante + '%',)

        cursor.execute(command, value)

        result = cursor.fetchall()

        cursor.close()
        connection.close()
        return result

    def search_all_visit_accept(self):
        connection = self.database.connect()
        cursor = connection.cursor()

        command = """SELECT * FROM pedidos_aprovados NATURAL JOIN pedido_de_visita"""

        cursor.execute(command)

        result = cursor.fetchall()

        cursor.close()
        connection.close()
        return result

    def update_visit_accept(self, escolha, cod_aprovado, id_pedido=None, nome_aprovador=None):
        match escolha:
            case "1":  # Só o id_pedido
                command = "UPDATE pedidos_aprovados SET id_pedido = %s WHERE cod_aprovado = %s"
                value = (id_pedido, cod_aprovado)

                self.execute_and_close(command, value)
            case "2":  # Só o nome_aprovador
                command = "UPDATE pedidos_aprovados SET nome_aprovador = %s WHERE cod_aprovado = %s"
                value = (nome_aprovador, cod_aprovado)

                self.execute_and_close(command, value)
            case "3":  # Nome aprovador e id pedido
                command = "UPDATE pedidos_aprovados SET nome_aprovador = %s, id_pedido = %s WHERE cod_aprovado = %s"
                value = (nome_aprovador, id_pedido, cod_aprovado)

                self.execute_and_close(command, value)

    def delete_visit_accept(self, cod_aprovado):
        command = "DELETE FROM pedidos_aprovados WHERE cod_aprovado = %s"
        value = (cod_aprovado,)

        self.execute_and_close(command, value)

    def check_existence_request(self, id_visitante):
        connection = self.database.connect()
        cursor = connection.cursor()

        command = "SELECT * FROM pedido_de_visita WHERE id_pedido = %s"
        value = (id_visitante,)

        cursor.execute(command, value)

        result = cursor.fetchall()
        print(result)

        cursor.close()
        connection.close()
        return result

    def execute_and_close(self, command, value=None):
        connection = self.database.connect()
        cursor = connection.cursor()
        cursor.execute(command, value)
        connection.commit()
        cursor.close()
        connection.close()


if __name__ == "__main__":
    operations = CrudVisitRequest()
