import math

from scipy.special import iv


def calculate_B(alpha_0, gamma, R, T_inf, M, T_w, S, pho, D, T_aw):
    # 计算变形贝塞尔函数
    I0 = iv(0, S ** 2 / 2)
    I1 = iv(1, S ** 2 / 2)

    # 计算公式中的各项
    term1 = T_aw - T_w
    term2 = math.exp(-(S ** 2 / 2))
    term3 = (1 + S ** 2) * I0 + S ** 2 * I1

    # 计算 b
    q = alpha_0 * (gamma + 1) / (gamma - 1) * D * pho * math.sqrt(math.pi * R * T_inf / 8 / M) * R / M * term1 * term2 * term3
    B = alpha_0 * (gamma + 1) / (gamma - 1) * D * math.sqrt(math.pi * R * T_inf / 8 / M) * R / M * term2 * term3
    return B

def calculate_T_aw(gamma, T_inf, S):
    # 计算变形贝塞尔函数
    I0 = iv(0, S ** 2 / 2)
    I1 = iv(1, S ** 2 / 2)

    # 计算各项
    term1 = (gamma - 1) / (gamma + 1)
    term2 = (3 * S**2 + 2 * S**4) * I0 + ( S**2 + 2 * S**4) * I1
    term3 = (1 + S**2 ) * I0 + S**2 * I1
    # 计算 T_aw
    T_aw = T_inf * (1 + term1 * term2 / term3)
    return T_aw



# 示例值
alpha_0 = 0.9  # 热协调系数
gamma = 1.4  # 比热比
R = 8.31451  # 气体常数 (J/(mol·K))
M = 28.97  # 分子量 (kg/mol)
D = 10**(-8) # 碳纳米管直径
pho = 2620 # 碳纳米管密度
T_inf = 323  # 气流温度 (K)
T_w = 298  # 壁面温度 (K)
C_p = 957.5 # 碳纳米管恒压热容 J/(kg·K)

u = 1 # 空气流速 单位：m/s
S = u / math.sqrt(2 * R * T_inf / M)  # 分子速率比

#q/l = B*(T_aw-T)*pho = pho*pi*(D/2)**2 *C_p*dT/dt

B = calculate_B(alpha_0, gamma, R, T_inf, M, T_w, S, pho, D, calculate_T_aw(gamma, T_inf, S))
tau = math.pi * (D/2)**2 * C_p / B
print(f"计算得到的 B 值为: {B}")
print(f"计算得到的 T_aw 值为: {calculate_T_aw(gamma, T_inf, S)}")
print(f"计算得到的 tau 值为: {tau}")