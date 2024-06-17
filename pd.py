import pandas as pd

dict1 = {
    "name":["nirav","indra","kalpo"],
    "marks":[282,253,293],
    "city":["Lakheni","Rajpara","Rajpara"]
}

df = pd.DataFrame(dict1)
print(df)