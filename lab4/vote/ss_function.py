import random

def quick_power(a: int, b: int, p: int) -> int:
    """
    快速幂算法：计算 (a^b) % p
    参数:
        a (int): 底数
        b (int): 指数
        p (int): 模数
    返回:
        int: 计算结果
    """
    a = a % p
    result = 1
    while b != 0:
        if b & 1:
            result = (result * a) % p
        b >>= 1
        a = (a * a) % p
    return result


def generate_polynomial(constant_term: int, degree: int, mod: int, name: str) -> list:
    """
    构建多项式：形式为 f(x) = a0 + a1x + a2x^2 + ... + adx^d
    参数:
        constant_term (int): 常数项系数
        degree (int): 多项式次数
        mod (int): 模数
        name (str): 多项式名称标识符
    返回:
        list: 多项式系数列表 [a0, a1, ..., ad]
    """
    coefficients = [constant_term]
    for _ in range(degree):
        coefficients.append(random.randint(0, mod - 1))
    
    # 输出多项式表达式
    polynomial_str = f'f{name} = {coefficients[0]}'
    for i in range(1, degree + 1):
        polynomial_str += f' + {coefficients[i]}x^{i}'
    print(polynomial_str)
    
    return coefficients


def evaluate_polynomial(coefficients: list, x: int, mod: int) -> int:
    """
    计算多项式在 x 处的值：f(x) % mod
    参数:
        coefficients (list): 多项式系数列表
        x (int): 输入值
        mod (int): 模数
    返回:
        int: 计算结果
    """
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        result = (result + coefficients[i] * quick_power(x, i, mod)) % mod
    return result


def reconstruct_polynomial(shares_x: list, shares_y: list, threshold: int, mod: int) -> int:
    """
    使用拉格朗日插值法重构多项式并计算 f(0)
    参数:
        shares_x (list): 已知点的 x 坐标
        shares_y (list): 对应的 y 值
        threshold (int): 需要使用的点数量
        mod (int): 模数（需为质数）
    返回:
        int: 重构后的 f(0) 值
    """
    result = 0
    for i in range(threshold):
        yi = shares_y[i] % mod
        xi = shares_x[i]
        
        # 计算拉格朗日基多项式 L_i(0)
        lagrange_term = 1
        for j in range(threshold):
            if i != j:
                xj = shares_x[j]
                denominator = quick_power(xi - xj, mod - 2, mod)  # 费马小定理求逆元
                lagrange_term = (-lagrange_term * xj * denominator) % mod
        
        result = (result + yi * lagrange_term) % mod
    return result