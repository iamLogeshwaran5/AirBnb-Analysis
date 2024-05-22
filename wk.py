# %%
from pymongo import MongoClient

client = MongoClient('mongodb+srv://logeshwaran1478:123456789Pass@cluster0.jyfzdnr.mongodb.net/?retryWrites=true&w=majority')


# %%
db = client.test

# %%
db

# %%
db = client['Cluster0']
col = db ['Airhub_collection']

# %%
col

# %%
for i in col.find():
    print(i)
    break


# %%
data=[]
for i in col.find():
    data.append(i)
print(data)

# %%
data[5554]

# %%
import pandas as pd

# Convert MongoDB cursor to DataFrame
df = pd.DataFrame(data)

# %%
df.shape

# %%
df.head(3)

# %%
df.describe()

# %%
df.info()

# %%
df.isnull().sum()

# %% [markdown]
# #Drop columns On the basis of:-
# #1. least importance
# #2. unique features
# #3. null values

# %%
data = df.drop(['_id','listing_url','summary','name','space','description','neighborhood_overview','notes','transit','access','interaction','house_rules','amenities', 'images', 'host', 'address', 'availability', 'review_scores', 'reviews','reviews_per_month','monthly_price','weekly_price','first_review','last_review','cleaning_fee','security_deposit'], axis = 'columns')

# %%
data.head(10)

# %%
# List of columns to remove
columns_to_remove = ['date', 'some_key']

# Remove columns from the DataFrame if they exist
data.drop(columns=[col for col in columns_to_remove if col in data.columns], inplace=True)

print(data.head())


# %%
data.head(10)

# %%
data.isnull().sum()

# %%
data.isnull().sum()

# %%
data.shape

# %%
data.head(3)

# %%
data.to_csv('C:/Users/wolfr/OneDrive/Desktop/Logeshwaran_WorkSpace/Airbnb_Analysis/Airbnb.csv', index = True )


