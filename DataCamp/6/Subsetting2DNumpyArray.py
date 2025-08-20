import numpy as np

np_baseball = np.array(baseball)

# 1. Print out the 50th row of np_baseball
print(np_baseball[49, :])   # 49 because Python indexing starts at 0

# 2. Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)

# 3. Print out height (first column) of the 124th player
print(np_baseball[123, 0])  # 123 for the 124th player
