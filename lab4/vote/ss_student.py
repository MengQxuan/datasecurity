import ss_function as ss_f

def main():
    # 设置模数
    MODULUS = 1000000007
    print(f'模数 p：{MODULUS}')
    
    # 获取用户输入
    participant_id = int(input("请输入参与方 id:"))
    secret_value = int(input(f'请输入 student_{participant_id}的投票值 s:'))
    
    # 初始化秘密份额
    shares_x = [1, 2, 3]
    shares_y = []
    
    # 生成多项式和秘密份额
    print(f'Student_{participant_id}的投票值的多项式及秘密份额：')
    polynomial = generate_and_display_polynomial(secret_value, shares_x, MODULUS, participant_id)
    generate_shares(polynomial, shares_x, shares_y, MODULUS)
    
    # 分发秘密份额到文件
    distribute_shares(participant_id, shares_y)

def generate_and_display_polynomial(s, x_values, p, id_suffix):
    """生成多项式并显示表达式"""
    polynomial = ss_f.generate_polynomial(s, 1, p, str(id_suffix))
    for x in x_values:
        fx = ss_f.evaluate_polynomial(polynomial, x, p)
        print(f'({x},{fx})')
    return polynomial

def generate_shares(polynomial, x_values, shares_y, p):
    """计算所有秘密份额"""
    for x in x_values:
        shares_y.append(ss_f.evaluate_polynomial(polynomial, x, p))

def distribute_shares(participant_id, shares_y):
    """将份额写入对应文件"""
    for i in range(1, 4):
        filename = f'student_{participant_id}_{i}.txt'
        with open(filename, 'w') as f:
            f.write(str(shares_y[i-1]))

if __name__ == "__main__":
    main()