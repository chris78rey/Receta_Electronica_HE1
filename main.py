from receta.componentes.inicio import Infraestructura

import sched
import time


class PeriodicScheduler(object):
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def setup(self, interval, action, actionargs=()):
        action(*actionargs)
        self.scheduler.enter(interval, 1, self.setup,
                             (interval, action, actionargs))

    def run(self):
        self.scheduler.run()


infraestructura = Infraestructura('C:\\data\\', 'christian19782013@gmail.com')

for bucle in range(1000000):
    try:
        # time.sleep(1)
        infraestructura.ejecuta_flujo()
    except Exception as e:
        print(e.message)
#
# INTERVAL = 20  # every
# periodic_scheduler = PeriodicScheduler()
# periodic_scheduler.setup(INTERVAL, infraestructura.ejecuta_flujo)  # it executes the event just once
# periodic_scheduler.run()  # it st    arts the scheduler
