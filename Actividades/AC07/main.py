from utils.parser import ApacheLogsParser


class BigAnalizador:

    def __init__(self, logs):
        self.logs = logs

    def bytes_transferidos(self):
        # Completar
        pass

    def errores_servidor(self):
        # Completar
        pass

    def solicitudes_exitosas(self):
        # Completar
        pass

    def url_mas_solicitada(self):
        # Completar
        pass

if __name__ == '__main__':
    parser = ApacheLogsParser("./utils/nasa_logs_week.txt")
    logs = parser.get_apache_logs()
    biganalizador = BigAnalizador(logs)

    biganalizador.bytes_transferidos()
    biganalizador.errores_servidor()
    biganalizador.solicitudes_exitosas()
    biganalizador.url_mas_solicitada()
