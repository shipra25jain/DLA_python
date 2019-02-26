import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cross_validation import train_test_split
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
regr = linear_model.LinearRegression(fit_intercept= True, normalize=True)
df = pd.read_csv("dataforanalysis.csv")


X = df[["L2distance"]]
y = df[["stickiness"]]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.33, random_state=3)
regr.fit(X_train,y_train)
print("R2_score for L2distance: ", r2_score(y_test,regr.predict(X_test)))
plt.scatter(X_train,y_train,color = "red")
plt.plot(X_train,regr.predict(X_train),color = "blue")
plt.xlabel("L2distance")
plt.ylabel("stickiness")
plt.title("Residual Graph for L2distance")
plt.savefig("L2distance.png", dpi = 300)
print("intercept: ", regr.intercept_)
print("coefficient: ", regr.coef_)
plt.close()


X = df[["maxdistance"]]
y = df[["stickiness"]]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.33, random_state=3)
regr.fit(X_train,y_train)
print("R2_score for maxdistance: ", r2_score(y_test,regr.predict(X_test)))
plt.scatter(X_train,y_train,color = "red")
plt.plot(X_train,regr.predict(X_train),color = "blue")
plt.xlabel("maxdistance")
plt.ylabel("stickiness")
plt.title("Residual Graph for maxdistance")
plt.savefig("maxdistance.png", dpi = 300)
print("intercept: ", regr.intercept_)
print("coefficient: ", regr.coef_)
plt.close()

X = df[["numneighbour"]]
y = df[["stickiness"]]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.33, random_state=3)
regr.fit(X_train,y_train)
print("R2_score for numneighbour: ", r2_score(y_test,regr.predict(X_test)))
plt.scatter(X_train,y_train,color = "red")
plt.plot(X_train,regr.predict(X_train),color = "blue")
plt.xlabel("numneighbour")
plt.ylabel("stickiness")
plt.title("Residual Graph for numneighbour")
plt.savefig("numneighbour.png", dpi = 300)
print("intercept: ", regr.intercept_)
print("coefficient: ", regr.coef_)
plt.close()

X = df[["maxradius"]]
y = df[["stickiness"]]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.33, random_state=3)
regr.fit(X_train,y_train)
print("R2_score for maxradius: ", r2_score(y_test,regr.predict(X_test)))
plt.scatter(X_train,y_train,color = "red")
plt.plot(X_train,regr.predict(X_train),color = "blue")
plt.xlabel("maxradius")
plt.ylabel("stickiness")
plt.title("Residual Graph for maxradius")
plt.savefig("maxradius.png", dpi = 300)
print("intercept: ", regr.intercept_)
print("coefficient: ", regr.coef_)
plt.close()

