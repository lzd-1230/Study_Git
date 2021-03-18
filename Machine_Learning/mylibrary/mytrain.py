#-*-coding:GBK-*-
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.base import clone
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import Pipeline

def plot_learning_curves(model,X,y):
    """
    该函数用于对训练集进行带验证的训练(sklearn)
    输入参数:
        ① model:模型对象
        ② X:训练集
        ③ y:训练集标签
    随着学习样本的逐步增加,最终的模型表现曲线
    """
    X_train, X_val, y_train, y_val = train_test_split(X,y,test_size = 0.2)  # 这里可以设置用多少作验证集
    train_errors, val_errors = [],[]
    for m in range(1,len(X_train)):
        model.fit(X_train[:m],y_train[:m])
        y_train_pre = model.predict(X_train[:m])
        y_val_pre = model.predict(X_val)
        train_errors.append(mean_squared_error(y_train[:m],y_train_pre))
        val_errors.append(mean_squared_error(y_val,y_val_pre))
    plt.plot(np.sqrt(train_errors),"r-+",linewidth=2,label="train")
    plt.plot(np.sqrt(val_errors),"b-",linewidth=2,label="val")
    plt.legend()
    plt.show()

def stop_train_poly(model,X,y,dgre):
    """
    该函数是自带提前终止的批量梯度下降训练,以多项式回归为例子(sklearn)
    输入参数:
        ① model:模型对象
        ② X:训练集
        ③ y:训练集标签
    注:可以结合前面的学习曲线图
        ???如果想让他提手动结束的时候也具有返回值怎么做到呢?

    """
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    poly_scaler = Pipeline([("ploy_features",PolynomialFeatures(degree=dgre,include_bias=False)),
                     ("std_scaler",StandardScaler())
                     ])
    X_train_poly_scaled = poly_scaler.fit_transform(X_train)
    X_val_poly_scaled = poly_scaler.transform(X_val)

    # 开始梯度下降
    sgd_reg = SGDRegressor(max_iter=1, tol=-np.infty, warm_start=True,  # 这个参数是让模型接着训练
                           penalty=None, learning_rate="constant", eta0=0.0005)
    minimum_val_error = float("inf")
    best_epoch = None
    best_model = None
    val_error_list = []

    # 重复不停地训练,直到在验证集上的结果变差!
    for epoch in range(100):
        sgd_reg.fit(X_train_poly_scaled,np.ravel(y_train))
        y_val_pre = sgd_reg.predict(X_val_poly_scaled)

        val_error = mean_squared_error(y_val_pre,y_val)
        print(f"均方误差为:{val_error}")
        val_error_list.append(val_error)
        if val_error < minimum_val_error:
            minimum_val_error = val_error
            best_epoch = epoch
            best_model = clone(sgd_reg)

    plt.plot(np.sqrt(val_error_list),"r-+",linewidth=2,label="val_error")
    plt.legend()
    plt.show()