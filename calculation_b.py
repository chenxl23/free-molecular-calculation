import numpy as np
from scipy.optimize import fsolve

# 定义已知参数
beta = 4.3  # mm
a = 10e-6   # 10 nm 转换为 mm

# 定义方程
def equation(b):
    return b * np.log(b / a) - 2 * beta

# 提供一个初始猜测值
initial_guess = 4.3  # mm, 根据之前的讨论选择接近这个值

# 使用fsolve求解
b_solution, = fsolve(equation, initial_guess)

print(f"气膜厚度 b 的数值解为: {b_solution:.6f} mm")