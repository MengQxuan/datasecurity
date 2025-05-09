import ss_function as ss_f

# 设置模数 p（需为大素数，用于模运算保证安全性）
p = 1000000007

# 随机选取两个参与方（如 student2 和 student3）进行秘密重构
# 读取其他参与方存储的秘密份额 d2 和 d3
d_23 = []
for i in range(2, 4):
    # 打开并读取存储在对应文件中的秘密份额值
    with open(f'd_{i}.txt', "r") as f:
        d_23.append(int(f.read()))  # 将文本内容转换为整数并存入列表

# 使用拉格朗日插值法重构原始秘密值 d = a + b + c
d = ss_f.reconstruct_polynomial([2, 3], d_23, 2, p)
# 计算平均值
d = d / 3
# 输出最终投票结果
print(f'得票结果为：{d}')