import pandas as pd
import numpy as np
data = pd.DataFrame({'A':np.random.randint(1,100,10),
                     'B':np.random.randint(1,100,10),
                     'C':np.random.randint(1,100,10)})
print(data)
print(data.corr())
print(data.corr('kendall'))
print(data.corr('spearman'))
