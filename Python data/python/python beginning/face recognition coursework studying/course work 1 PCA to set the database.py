import numpy as np
o = np.array([[84,65,61,72,79,81],[64,77,77,76,55,70],[65,67,63,49,57,67],[74,80,69,75,63,74],[84,74,70,80,74,82]])
o_mean = np.mean(o, axis=0) # compute mean
print(o_mean)
m = np.subtract(o, o_mean)  # zero-mean
COV = np.dot(m.T, m)  # cov gian
w, v = np.linalg.eig(COV)  # feature gain
print(w)
print(v)
# 计算主成分贡献率以及累计贡献率
sum_lambda = np.sum(w)  # 特征值的和
print(sum_lambda)
f = np.divide(w, sum_lambda)  # 每个特征值的贡献率（特征值 / 总和）
print(f)
print(f[0]+f[1])
e1 = v.T[0]
