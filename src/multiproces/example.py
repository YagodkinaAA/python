import multiprocessing


def worker(i):
    print(f'Worker-{i}')


procs = []
for i in range(5):
    p = multiprocessing.Process(target=worker, args=(i,))
    procs.append(p)
    p.start()

print('Ждем результаты...')
[proc.join() for proc in procs]
print('Результаты получены.')