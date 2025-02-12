# 4145-A1
ITCS 4145 Assignment1 MergSort

This program implements Merge Sort algorithm in C++.
It first generates a integer array in random manner and sorts it using mergeSort() then prints the time taken to sort the array.



But before you begin, make sure you have access to 
- A Linux-based system with SLURM workload management
- gcc compiler (this is critical to execute the program)
- Access to hpc lab computer Centaurus
- UNC Charlotte VPN if you are outside of campus or not using "eduroam" network
- Python 3 with pandas and matplotlib libraries for chart.py



Steps to compile and experiment:

1. Connecting hpc lab computer by "ssh hpc-student.charlotte.edu -l your-username"
2. Authenticate with Duo
3. Type "g++ A1-4145.cpp -o 4145-A1" a1 is the name of the executable file and A1-4145 is the original code name. g++ allows us to make executable file.
4. Schedule the job by "sbatch 4145-A1.sh"
5. Outcome should be something like "Submitted batch job [????]", pay attention to the number.
6. Wait a bit for command to finish running and record the time it takes. 
7. If you would like a csv file recording the time, type "sbatch 4145-A1.sh > timelog.csv". It will schedule the job and record the time onto csv file called timelog.csv. You can name the file whatever you desire, but this timelog is what I named. 
8. To create a chart or visualize the  time increase, type "python chart.py" and it creates "Timelog.png" which is a png file of linear chart. 



Keys:
- Generated numbers are from rand() function and it's between 0-9999.
- The sorting time is printed to stderr, making sure that it does not interfere with other output.
- When you type numbers for how big the array is, it has to be positive number in order to run without the fail. If you type <0 integer after "./4145-A1" in .sh file, yoou will get a "Error: Array size must be a positive integer."



Records:
- 10^1 = Time taken to sort 10 elements: 4.839e-06 seconds
- 10^2 = Time taken to sort 100 elements: 4.5972e-05 seconds
- 10^3 = Time taken to sort 1000 elements: 0.00050224 seconds
- 10^4 = Time taken to sort 10000 elements: 0.0056795 seconds
- 10^5 = Time taken to sort 100000 elements: 0.0629707 seconds
- 10^6 = Time taken to sort 1000000 elements: 0.67559 seconds
- 10^7 = Time taken to sort 10000000 elements: 7.21877 seconds
- 10^8 = Time taken to sort 100000000 elements: 77.049 seconds
- 10^9 = Time taken to sort 1000000000 elements: 834.524 seconds



Insight:
As the number of the integer increases, the time insreased as well. The increase is about 10 times more which also makes sense since we are increasing the number of integer by 10, creating linear increase.

