import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from extract_floor_info import extract_floor_info

rent_data = pd.read_csv("../data/raw/house_rent_dataset.csv")

# data cleaning
cleaned_data = rent_data.drop(columns=["Posted On", "Point of Contact", "Area Locality"])

# data transformation
cols = ["Furnishing Status", "Tenant Preferred", "Area Type", "City"]

encoder = OneHotEncoder(
    drop="first", 
    sparse_output=False, 
    handle_unknown="ignore"
)

encoded = encoder.fit_transform(cleaned_data[cols])
encoded_data = pd.DataFrame(
    encoded, 
    columns=encoder.get_feature_names_out(cols), 
    index=cleaned_data.index
)

cleaned_data = pd.concat(
    [cleaned_data.drop(columns=cols), encoded_data], 
    axis=1
)

## transform floor info
cleaned_data[["Current Floor", "Total Floors"]] = (
    cleaned_data["Floor"]
    .apply(extract_floor_info)
)

cleaned_data.drop("Floor", axis=1, inplace=True)