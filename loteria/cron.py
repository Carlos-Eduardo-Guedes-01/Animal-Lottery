import schedule
import time
from tasks import minha_tarefa, sorteia_numero, procura_ganhador

#schedule.every().day.at("22:30").do(sorteia_numero)
schedule.every().day.at("22:59").do(procura_ganhador)

while True:
    schedule.run_pending()
    time.sleep(1)