import schedule
import time
from tasks import minha_tarefa, sorteia_numero, procura_ganhador,sorteio_, procura_ganhador_bicho

schedule.every().day.at("18:00").do(sorteia_numero)
schedule.every().day.at("18:01").do(procura_ganhador)
schedule.every().day.at("18:02").do(sorteio_)
schedule.every().day.at("18:03").do(procura_ganhador_bicho)

while True:
    schedule.run_pending()
    time.sleep(1)