# 设置模数 p（需为大素数，用于模运算保证安全性）
p = 1000000007
# 输入当前参与方的 id（需与生成阶段保持一致）
id = int(input("请输入参与方 id:"))

# 读取其他参与方分享给当前参与方的秘密份额
# 每个文件 student_i_id.txt 存储了由第 i 个参与方生成的份额
data = []
for i in range(1, 4):
    # 打开并读取存储在对应文件中的秘密份额值
    with open(f'student_{i}_{id}.txt', "r") as f:
        data.append(int(f.read()))  # 将文本内容转换为整数并存入列表

# 计算三个秘密份额的和（模 p 运算），每个数据项对应一个秘密份额，总共有 3 个份额
d = 0
for i in range(0, 3):
    d = (d + data[i]) % p  # 累加并保持模 p 运算

# 将计算结果保存到 d_id.txt 文件，该文件将用于后续的秘密重构阶段
with open(f'd_{id}.txt', 'w') as f:
    f.write(str(d))  # 写入计算后的秘密份额值