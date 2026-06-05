from sklearn.linear_model import LinearRegression
import numpy as np

numeric_cols = traffic_two_month.select_dtypes(include="number").columns

target = st.selectbox(
    "Select Forecast Column",
    numeric_cols
)

data = traffic_two_month[target].dropna()

X = np.arange(len(data)).reshape(-1,1)
y = data.values

model = LinearRegression()
model.fit(X,y)

future_x = np.arange(len(data)+30).reshape(-1,1)

predictions = model.predict(future_x)
