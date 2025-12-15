from src.scheduling.process import Process
from src.scheduling.scheduler import PriorityAgingScheduler


def test_scheduler_completes_all():
    procs = [
        Process(pid="P1", arrival=0, burst=5, base_priority=3),
        Process(pid="P2", arrival=1, burst=3, base_priority=1),
        Process(pid="P3", arrival=2, burst=2, base_priority=2),
    ]
    sched = PriorityAgingScheduler(aging_interval=10)
    res = sched.run(procs)

    assert set(res.completion_times.keys()) == {"P1", "P2", "P3"}
    assert res.average_waiting_time >= 0
    assert len(res.timeline) > 0
