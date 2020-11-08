# python3
import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker:
    """Worker class.
    The workers are sorted by release time. If the release time is the same for
    both of them, workers are sorted by their thread_id.
    """

    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time



def assign_jobs(n_workers, jobs):
    result = []
    worker_queue = [Worker(i) for i in range(n_workers)]
    for job in jobs:
        worker = heapq.heappop(worker_queue)
        result.append((worker.thread_id, worker.release_time))
        worker.release_time += job
        heapq.heappush(worker_queue, worker)
    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    results = assign_jobs(n_workers, jobs)

    for worker_id, start_time in results:
        print(worker_id, start_time)


if __name__ == "__main__":
    main()
