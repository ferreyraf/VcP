import pandas as pd
import numpy as np

X = np.empty([4,2],dtype=int)
Y = np.empty([4,2],dtype=int)

print(f"\t\tMatrix X.\n {X}\n")
print(f"\t\tMatrix Y.\n {Y}\n")


# Forams de implementar un DataFrame

df = pd.DataFrame(
    {
        "Name" : ["name1","name1",
        ],
        "Cosas" : ["Think1",2,
        ],
    }
)

print(df)