import pandas as panda
import matplotlib.pyplot as pylt

data = [
    ("Time taken to sort 10 elements:", 4.839e-06),
    ("Time taken to sort 100 elements:", 4.5972e-05),
    ("Time taken to sort 1000 elements:", 0.00050224),
    ("Time taken to sort 10000 elements:", 0.0056795),
    ("Time taken to sort 100000 elements:", 0.0629707),
    ("Time taken to sort 1000000 elements:", 0.67559),
    ("Time taken to sort 10000000 elements:", 7.21877),
    ("Time taken to sort 100000000 elements:", 77.049),
    ("Time taken to sort 1000000000 elements:", 834.524)
]

d = panda.DataFrame(data, columns=["Description", "Time"])

d["Elements"] = d["Description"].apply(lambda x: int(x.split()[4]))

pylt.plot(d["Elements"], d["Time"], marker="o", linestyle="-", color="b", label="Sort Time")

pylt.xlabel("Number of Integers")
pylt.ylabel("Time (s)")
pylt.title("Execution Time of MergeSort")
pylt.xscale('log')
pylt.yscale('log')
pylt.legend()
pylt.grid(True)

pylt.savefig("Timelog.pdf", format="pdf")

pylt.show()
