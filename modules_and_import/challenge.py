import time
import webbrowser

print("perf_counter: ", time.get_clock_info("perf_counter"))
print("monotonic: ", time.get_clock_info("monotonic"))
print("process_time: ", time.get_clock_info("process_time"))

help(time.perf_counter)
help(time.monotonic)
help(time.perf_counter)

webbrowser.open("https://docs.python.org/3.8/library/time.html#time.perf_counter")
webbrowser.open("https://docs.python.org/3.8/library/time.html#time.monotonic")
webbrowser.open("https://docs.python.org/3.8/library/time.html#time.process_time")

# using perf_counter
start_perf = time.perf_counter()
time.sleep(1)
end_perf = time.perf_counter()
print("perf: {}".format(end_perf - start_perf))

start_mono = time.monotonic()
time.sleep(1)
end_mono = time.monotonic()
print("mono: {}".format(end_mono - start_mono))

start_proc = time.process_time()
time.sleep(1)
end_proc = time.process_time()
print("proc: {}".format(end_proc - start_proc))
