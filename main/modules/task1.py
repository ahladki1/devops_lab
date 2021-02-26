#!/usr/bin/env python

import psutil
from datetime import datetime
import time
import json


def do_snapshot(tp):
    i = 1
    while True:
        sn = Snapshot()
        if tp == "txt":
            with open('snapshot.txt', 'a') as f:
                f.write("SNAPSHOT" + str(i) + ":"
                        + str(sn.time_st) + ":"
                        + str(sn.cpu) + "  "
                        + str(sn.memory) + "  "
                        + str(sn.v_memory) + "  "
                        + str(sn.io_inf_r) + "  "
                        + str(sn.io_inf_w) + "  "
                        + str(sn.net) + "  ")
            f.close()

        elif tp == "json":
            data = {"SNAPSHOT" + str(i) + ":" + str(sn.time_st): {
                "cpu": sn.cpu,
                "memory": sn.memory,
                "virtual_memory": sn.v_memory,
                "read_bytes": sn.io_inf_r,
                "write_bytes": sn.io_inf_w,
                "net": sn.net,
            }
            }

            with open('snapshot.json', 'a') as f:
                json.dump(data, f, ensure_ascii=False)
            f.close()
        else:
            print("Incorrect type for the file")
            break
        time.sleep(300)
        i += 1


class Snapshot:
    def __init__(self):
        self.now = datetime.now()
        self.time_st = datetime.timestamp(self.now)
        self.cpu = psutil.cpu_percent(1)
        self.memory = psutil.swap_memory()
        self.v_memory = psutil.virtual_memory()[2]
        self.io_inf_r = psutil.disk_io_counters().read_bytes
        self.io_inf_w = psutil.disk_io_counters().write_bytes
        self.net = psutil.net_if_stats()
