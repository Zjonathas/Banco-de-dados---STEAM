import mysql.connector as connector


class DataBase:
    def connect(self):
        """Realiza a conexão com o database da steam"""
        try:
            connetion = connector.connect(
                host="steam.mysql.database.azure.com",
                user="steam",
                password="ifrn@79025434",
                database="steam"
            )
            return connetion
        except connector.Error as erro:
            print(f"Erro ao conectar: {erro.msg}")


class CrudVisitRequest:
    def __init__(self):
        self.database = DataBase()
        self.connection = None
        self.cursor = None

    def insert_visit(self, nome_visitante, email_visitante, telefone_visitante):
        command = ("INSERT INTO pedido_de_visita(nome_visitante, email_visitante, telefone_visitante) VALUES "
                   "(%s, %s, %s)")
        value = (nome_visitante, email_visitante, telefone_visitante)

        self.execute_and_close(command, value)

    def search_visit(self, nome_visitante):
        connection = self.database.connect()
        cursor = connection.cursor()

        command = "SELECT * FROM pedido_de_visita WHERE nome_visitante = %s"
        value = (nome_visitante,)

        cursor.execute(command, value)

        result = cursor.fetchall()

        cursor.close()
        connection.close()
        return result

    def search_visit_id(self, id_visitante):
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

    def search_all_visit(self):
        connection = self.database.connect()
        cursor = connection.cursor()

        command = "SELECT * FROM pedido_de_visita"

        cursor.execute(command)

        result = cursor.fetchall()

        cursor.close()
        connection.close()
        return result

    def update_visit(self, escolha, id_visitante, nome_visitante=None, email_visitante=None, telefone_visitante=None):
        match escolha:
            case "1":  # Só o nome
                command = "UPDATE pedido_de_visita SET nome_visitante = %s WHERE id_pedido = %s"
                value = (nome_visitante, id_visitante)

                self.execute_and_close(command, value)
            case "2":  # Só o email
                command = "UPDATE pedido_de_visita SET email_visitante = %s WHERE id_pedido = %s"
                value = (email_visitante, id_visitante)

                self.execute_and_close(command, value)
            case "3":  # Só o telefone
                command = "UPDATE pedido_de_visita SET telefone_visitante = %s WHERE id_pedido = %s"
                value = (telefone_visitante, id_visitante)

                self.execute_and_close(command, value)
            case "4":  # nome e email
                command = ("UPDATE pedido_de_visita SET nome_visitante = %s, email_visitante = %s "
                           "WHERE id_pedido = %s")
                value = (nome_visitante, email_visitante, id_visitante)

                self.execute_and_close(command, value)
            case "5":  # nome e telefone
                command = ("UPDATE pedido_de_visita SET nome_visitante = %s, telefone_visitante = %s "
                           "WHERE id_pedido = %s")
                value = (nome_visitante, telefone_visitante, id_visitante)

                self.execute_and_close(command, value)
            case "6":  # email e telefone
                command = ("UPDATE pedido_de_visita SET email_visitante = %s, telefone_visitante = %s "
                           "WHERE id_pedido = %s")
                value = (email_visitante, telefone_visitante, id_visitante)

                self.execute_and_close(command, value)
            case "7":  # Tudo
                command = (
                    "UPDATE pedido_de_visita SET nome_visitante = %s, email_visitante = %s, telefone_visitante = %s "
                    "WHERE id_pedido = %s")
                value = (nome_visitante, email_visitante, telefone_visitante, id_visitante)

                self.execute_and_close(command, value)

    def delete_visit(self, id_pedido):
        command = "DELETE FROM pedido_de_visita WHERE id_pedido = %s"
        value = (id_pedido,)

        self.execute_and_close(command, value)

    def sing_up(self, user, password):
        command = """INSERT INTO usuario (usuario, senha) VALUES (%s, %s)"""
        value = (user, password)

        self.execute_and_close(command, value)

    def validate_user(self, user, password):
        connection = self.database.connect()
        cursor = connection.cursor()

        command = """SELECT usuario, senha FROM usuario WHERE usuario = %s and senha = %s"""
        value = (user, password)

        cursor.execute(command, value)
        result = cursor.fetchall()
        if not result:
            print('Usuário e/ou senha incorreto(s)')
            cursor.close()
            connection.close()
            return False
        return True

    def execute_and_close(self, command, value=None):
        connection = self.database.connect()
        cursor = connection.cursor()
        cursor.execute(command, value)
        connection.commit()
        cursor.close()
        connection.close()


if __name__ == "__main__":
    operations = CrudVisitRequest()
