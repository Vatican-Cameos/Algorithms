# Uses python3
#
# Problem Description
# Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
# Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item, respectively.
# Constraints. 1≤𝑛≤103,0≤𝑊 ≤2·106;0≤𝑣𝑖 ≤2·106,0<𝑤𝑖 ≤2·106 forall1≤𝑖≤𝑛.Allthe numbers are integers.
# Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute value of the difference between the answer of your program and the optimal value should be at most 10−3. To ensure this, output your answer with at least four digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
# Sample 1.
# Input:
# 3 50
# 60 20
# 100 50
# 120 30
# Output:
# 180.0000
# To achieve the value 180, we take the first item and the third item into the bag.
#
# Sample 2.
# Input:
# 1 10
# 500 30
# Output:
# 166.6667
# Here, we just take one third of the only available item.


import sys
from operator import itemgetter
def get_optimal_value(capacity, weights, values):
    value = 0.
    knapsackItems = list(zip(values, weights, [float(ai)/bi for ai,bi in zip(values,weights)]))
    knapsackItems.sort(key=lambda x: x[2], reverse=True)

    for i in range(len(knapsackItems)):
        weight = knapsackItems[i][1]
        valuePerUnit = knapsackItems[i][2]
        if capacity == 0:
            return value
        a = min(weight, capacity)
        value = value + a * valuePerUnit
        capacity = capacity - a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
