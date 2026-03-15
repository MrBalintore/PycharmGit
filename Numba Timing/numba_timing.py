
import threading
import time
import os

from numba import njit, prange
import numpy as np


@njit(nogil=True)
def heavy_compute(x, n):
    # n = 5_000_000
    # print(f"heavy compute n={n}")
    s = 0.0
    for i in range(n):
        s += (x + i) % 13
    return s


def worker(i, n):
    result = heavy_compute(i, n)
    #print(f"result {i} n={n}: {result}")

"""
in parallel worker n_threads=4 N=4000 n_loops=100
single_call= True
single call serial execution=0.027829647064208984

in parallel worker n_threads=4 N=4000 n_loops=100
single_call= True
single call serial execution=1.6840121746063232

parallel false
in parallel worker n_threads=32 N=4000 n_loops=1000
single_call= True
single call serial execution=15.66042685508728
parallel true

.......................
in parallel worker n_threads=32 N=4000 n_loops=100000
single_call= True
single call serial execution=0.9359643459320068

"""

@njit(nogil=True, parallel=False, fastmath=True)
def laplace_step(index, n_loops, u, out):
    """
    Compute one Laplace stencil update:
        out[i,j] = average of 4 neighbours of u[i,j]
    """
    nx, ny = u.shape
    # print(f"n_loops = {n_loops}")
    for i in prange(1, nx - 1):
        for j in range(1, ny - 1):
            for k in range(n_loops):
                out[i, j] = out[i, j] + 0.25 * (
                        u[i - 1, j] +
                        u[i + 1, j] +
                        u[i, j - 1] +
                        u[i, j + 1]
                )
    return True


def worker_2(i, n, input_array, output_qarray):
    result = laplace_step(i, n, input_array, output_qarray)
    # print(f"result {i} n={n}: {result}")

def serial_worker_harness(n_threads):
    n = 5_000_000
    n = 10_000_000
    n = 100_000_000
    n = 1_000_000_000
    configuration_dicts = [
        {"n_threads": 4, "N": 4000, "n": n},
        {"n_threads": 8, "N": 4000, "n": n},
        {"n_threads": 16, "N": 4000, "n": n},
        {"n_threads": 32, "N": 4000, "n": n},
    ]
    for configuration_dict in configuration_dicts:
        call_serial_worker(configuration_dict)

def call_serial_worker(configuration_dict):
    n = configuration_dict["n"]
    n_threads = configuration_dict["n_threads"]
    print(f"in serial worker n_threads={n_threads} n={n}")
    threads = [threading.Thread(target=worker, args=(i, n,)) for i in range(n_threads)]
    t0 = time.time()
    [t.start() for t in threads]
    [t.join() for t in threads]
    t1 = time.time()
    threaded_execution_time = t1 - t0
    print(f"overall threaded execution={threaded_execution_time}")

    t0 = time.time()
    for i in range(n_threads):
        heavy_compute(i, n)
    t1 = time.time()
    serial_execution_time = t1 - t0
    print(f"overall serial execution={serial_execution_time}")

    print(f"threaded_speed_up={serial_execution_time/threaded_execution_time}")

def parallel_worker_harness(n_threads, single_call=False):
    configuration_dicts = [
        {"n_threads": 4, "N": 4000, "n_inner_loops": 100},
        {"n_threads":  8, "N": 4000, "n_inner_loops": 100},
        {"n_threads": 16, "N": 4000, "n_inner_loops": 100},
        {"n_threads": 32, "N": 4000, "n_inner_loops": 100},
    ]
    if single_call:
        configuration_dict = {"n_threads": 32, "N": 4000, "n_inner_loops": 100000}
        call_parallel_worker(configuration_dict, single_call=single_call)
    else:
        for configuration_dict in configuration_dicts:
            call_parallel_worker(configuration_dict,single_call = single_call)

def call_parallel_worker(configuration_dict, single_call = False):
    "n_threads"
    # Example usage
    N         = configuration_dict["N"]
    n_inner_loops   = configuration_dict["n_inner_loops"]
    n_threads = configuration_dict["n_threads"]

    print(f"in parallel worker n_threads={n_threads} N={N} n_loops={n_inner_loops}")
    u = np.random.rand(N, N)
    out = np.zeros_like(u)
    laplace_step(0, n_threads, u, out)  # warmup (JIT compile)

    print("single_call=", single_call)
    if single_call:
        t0 = time.time()
        worker_2(0, n_inner_loops, u, out)
        t1 = time.time()
        serial_execution_time = t1 - t0
        print(f"single call serial execution={serial_execution_time}")
    else:
        threads = [threading.Thread(target=worker_2, args=(i, n_inner_loops, u, out,)) for i in range(n_threads)]
        t0 = time.time()
        [t.start() for t in threads]
        [t.join() for t in threads]
        t1 = time.time()
        threaded_execution_time = t1 - t0
        print(f"overall threaded execution={threaded_execution_time}")

        t0 = time.time()
        for i in range(n_threads):
            worker_2(i, n_inner_loops, u, out)
        t1 = time.time()
        serial_execution_time = t1 - t0
        print(f"overall serial execution={serial_execution_time}")

        print(f"threaded_speed_up={serial_execution_time/threaded_execution_time}")

if __name__ == "__main__":
    debug_level = 0
    os.environ["NUMBA_PARALLEL_DIAGNOSTICS"] = str(debug_level)
    n_threads = 4
    #serial_worker_harness(n_threads)
    #parallel_worker_harness(n_threads)
    #parallel_worker_harness(n_threads, single_call=True)

"""
--------------------------------------------------------
on david's PC
-------------------------------------------------------

.............david's PC..........................
in parallel worker n_threads=4 N=4000 n_loops=100
overall threaded execution=1.6809232234954834
overall serial execution=6.288078308105469
threaded_speed_up=3.7408480174540015
in parallel worker n_threads=8 N=4000 n_loops=100
overall threaded execution=1.8397181034088135
overall serial execution=12.430934190750122
threaded_speed_up=6.756977695505005
in parallel worker n_threads=16 N=4000 n_loops=100
overall threaded execution=2.2811710834503174
overall serial execution=24.954914569854736
threaded_speed_up=10.939519070226826
in parallel worker n_threads=32 N=4000 n_loops=100
overall threaded execution=4.677047967910767
overall serial execution=50.112038135528564
threaded_speed_up=10.714458880761399
.............david's PC..................................
in serial worker n_threads=4 n=1000000000
overall threaded execution=1.8958778381347656
overall serial execution=5.29535984992981
threaded_speed_up=2.793091275933464
in serial worker n_threads=8 n=1000000000
overall threaded execution=1.8135952949523926
overall serial execution=10.5650475025177
threaded_speed_up=5.825471389301899
in serial worker n_threads=16 n=1000000000
overall threaded execution=2.8118133544921875
overall serial execution=21.202318906784058
threaded_speed_up=7.540443206484873
in serial worker n_threads=32 n=1000000000
overall threaded execution=5.606244325637817
overall serial execution=43.225988149642944
threaded_speed_up=7.710328990116777
-------------------------------------------------

-------------------------------------------------------
seriial worker
n_threads = 4
overall threaded execution=1.9913275241851807
overall serial execution=5.377438068389893
theaded_speed_up=2.7004287356447074

n_threads=8
overall threaded execution=2.2428226470947266
overall serial execution=10.65008282661438
theaded_speed_up=4.748517605888331

n_threads =16
overall threaded execution=3.2929558753967285
overall serial execution=21.640478372573853
theaded_speed_up=6.571748663339332

n_threads=32
overall threaded execution=6.058661937713623
overall serial execution=42.595540046691895
theaded_speed_up=7.030519359653579

--------------------------------------------------------------------------


---------------------------------------------------
python can get a factor of 2 with theading

with njit
------------>
n=10 000 000 000 - ten billion loops
overall threaded execution=28.93113923072815
overall serial execution=56.36372971534729 - 50 time faster tha Python

without njit - i.e. standard Python
n=100,000,000  - one hunderd million loops
overall threaded execution=26.33606743812561
overall serial execution=26.834789514541626

njit allows threading to occur - and threading gives a factor of 2
...................................................................

with
@njit(nogil=False)
result 0 n=10000000000: 59999999985.0

overall threaded execution=57.23405194282532
overall serial execution=56.348751068115234

nogil has to be True for threading to occur
.............................................

======================================================================
@njit(parallel=True, fastmath=True)

overall threaded execution=16.26775550842285
overall serial execution=14.496626615524292

@njit(parallel=False, fastmath=True)
overall threaded execution=38.59339141845703     # from this and below - we can see nogil is False by default
overall serial execution=38.542036294937134

@njit(nogil=True, parallel=False, fastmath=True) # from this and above - we can see nogil allows multi-threading to work
overall threaded execution=13.784545183181763    #  multi-threading gain is 2.92 - more than 2 !!!!
overall serial execution=38.52716040611267

@njit(nogil=False, parallel=False, fastmath=True) # confirmation of top
overall threaded execution=38.65678787231445
overall serial execution=38.53246188163757

@njit(nogil=True, parallel=True, fastmath=True)  #
overall threaded execution=14.001735925674438    # paralle does not improve threaded performance
overall serial execution=14.171623229980469      #

@njit(nogil=False, parallel=True, fastmath=True)
overall threaded execution=13.793499946594238   # parallel removes benefor of threding
overall serial execution=15.623200178146362

switching on nogil or parallel gives the same speed up for threaded code
need parallel to speed up serial code factor of 2.7

============================== EXPECTED =====================================
Typical speed-ups on a 4–8 core CPU:
Pure Python10–20 seconds1×
Numba (single-thread)~0.2–0.5 seconds30×–50×
Numba (parallel=True)~0.05–0.2 seconds4×–6× more on top
"""

