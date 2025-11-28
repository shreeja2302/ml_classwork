import pandas as pd
import numpy as np
data = []
for i in range(1, 21):  
    height = np.random.randint(140, 200)
    weight = np.random.randint(40, 120)
    gender = np.random.choice(['Male', 'Female', 'Other'])
    age = np.random.randint(18, 70)

    data.append([height, weight, gender, age])
df = pd.DataFrame(data, columns=['Height(cm)', 'Weight(kg)', 'Gender', 'Age'])
df.to_csv('dataset.csv')
print(df)

