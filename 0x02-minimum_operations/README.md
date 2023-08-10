Minumum operations 
To solve this problem, I  used a greedy approach where I keep copying the existing H characters and pasting them until we reach the desired number of H characters. We can keep track of the number of operations required to reach the desired number of H characters. The algorithm can be implemented as follows:
Initialize a variable operations to 0.
Initialize a variable H to 1.
While H is less than n, do the following:
a. If n is divisible by H, set operations to operations + 2 and set H to H * 2.
b. Otherwise, increment H by the current value of H and set operations to operations + 1.
If H is equal to n, return operations. Otherwise, return 0.
The time complexity of this algorithm is O(log n) and the space complexity is O(1).