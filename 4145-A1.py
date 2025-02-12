import pandas as pd
import matplotlib.pyplot as plt

data = [
    ("Time taken to sort 10 elements:", 4.839e-06),
    ("Time taken to sort 10 elements:", 4.5972e-05),
    ("Time taken to sort 10 elements:", 0.00050224),
    ("Time taken to sort 10 elements:", 0.0056795),
    ("Time taken to sort 10 elements:", 0.0629707),
    ("Time taken to sort 10 elements:", 0.67559),
    ("Time taken to sort 10 elements:", 7.21877),
    ("Time taken to sort 10 elements:", 77.049),
    ("Time taken to sort 10 elements:", 834.524)
]

df = pd.DataFrame(data, columns=["Description", "Time"])

df["Elements"] = df["Description"].apply(lambda x: int(x.split()[1]))

plt.plot(df["Elements"], df["Time"], marker="o", linestyle="-", color="b", label="Sort Time")

plt.xlabel("Number of Integers")
plt.ylabel("Time (s)")
plt.title("Execution Time of MergeSort")
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)

plt.savefig("Timelog.png", format="png")

plt.show()
