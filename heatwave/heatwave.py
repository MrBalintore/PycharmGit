
from pprint import pprint
import numpy as np

def sequence_to_probability(sequence, individual_probabilities):
    p = 1.0
    for i in range(len(sequence)):
        if sequence[i]:
            p *= individual_probabilities[i]
        else:
            p *= (1 - individual_probabilities[i])
    return p
"""
PyCharm Pro
Download
License ID:
LA5R8BS7ZZ
"""

def main():
    a = 0.9
    b = 0.8
    c = 0.7
    d = 0.8

    days  = [ a, b, c ]
    n_days = len(days)
    n_scenarios = pow(2, n_days)
    print(n_scenarios)
    scenarios = []
    for i in range(n_scenarios):
        #print(i)
        sequence = [ bool(i & (1 << d)) for d in range(n_days) ]
        #print(sequence)
        scenarios.append(sequence)

    pprint(scenarios)
    probabilities = [ sequence_to_probability(sequence, days) for sequence in scenarios ]
    pprint(probabilities)
    overall = sum(probabilities)
    print(f"overall={overall}")

if ( __name__ == "__main__" ):
   main()
