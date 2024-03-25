import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({

    'x':range(1,11),
    'y':[10,9,3,1,7,6,5,3,4,2]
})

# print(df)

df.plot(x='x',y='y',kind="density")
plt.title("This is the Density plot")
plt.show()