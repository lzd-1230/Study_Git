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
    �ú������ڶ�ѵ�������д���֤��ѵ��(sklearn)
    �������:
        �� model:ģ�Ͷ���
        �� X:ѵ����
        �� y:ѵ������ǩ
    ����ѧϰ������������,���յ�ģ�ͱ�������
    """
    X_train, X_val, y_train, y_val = train_test_split(X,y,test_size = 0.2)  # ������������ö�������֤��
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
    �ú������Դ���ǰ��ֹ�������ݶ��½�ѵ��,�Զ���ʽ�ع�Ϊ����(sklearn)
    �������:
        �� model:ģ�Ͷ���
        �� X:ѵ����
        �� y:ѵ������ǩ
    ע:���Խ��ǰ���ѧϰ����ͼ
        ???������������ֶ�������ʱ��Ҳ���з���ֵ��ô������?

    """
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    poly_scaler = Pipeline([("ploy_features",PolynomialFeatures(degree=dgre,include_bias=False)),
                     ("std_scaler",StandardScaler())
                     ])
    X_train_poly_scaled = poly_scaler.fit_transform(X_train)
    X_val_poly_scaled = poly_scaler.transform(X_val)

    # ��ʼ�ݶ��½�
    sgd_reg = SGDRegressor(max_iter=1, tol=-np.infty, warm_start=True,  # �����������ģ�ͽ���ѵ��
                           penalty=None, learning_rate="constant", eta0=0.0005)
    minimum_val_error = float("inf")
    best_epoch = None
    best_model = None
    val_error_list = []

    # �ظ���ͣ��ѵ��,ֱ������֤���ϵĽ�����!
    for epoch in range(100):
        sgd_reg.fit(X_train_poly_scaled,np.ravel(y_train))
        y_val_pre = sgd_reg.predict(X_val_poly_scaled)

        val_error = mean_squared_error(y_val_pre,y_val)
        print(f"�������Ϊ:{val_error}")
        val_error_list.append(val_error)
        if val_error < minimum_val_error:
            minimum_val_error = val_error
            best_epoch = epoch
            best_model = clone(sgd_reg)

    plt.plot(np.sqrt(val_error_list),"r-+",linewidth=2,label="val_error")
    plt.legend()
    plt.show()