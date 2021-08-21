from fila_base import FilaBase

class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def atualiza_fila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chama_cliente(self, caixa:int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')