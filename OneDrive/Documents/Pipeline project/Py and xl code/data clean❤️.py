import pandas as pd
import numpy as np

INPUT_FILE = "vehicle_sales_tables.csv.xlsx"
OUTPUT_FILE = "vehicle_sales_cleaned.csv.xlsx"

# Read sheets
sales = pd.read_excel(INPUT_FILE, sheet_name="fact_sales")
customer = pd.read_excel(INPUT_FILE, sheet_name="dim_customer")
vehicle = pd.read_excel(INPUT_FILE, sheet_name="dim_vehicle")
location = pd.read_excel(INPUT_FILE, sheet_name="dim_location")
date_dim = pd.read_excel(INPUT_FILE, sheet_name="dim_date")

# =====================================
# FACT SALES
# =====================================

# Remove duplicates
sales = sales.drop_duplicates()

# Convert date
sales["sale_date"] = pd.to_datetime(sales["sale_date"])

# Fill missing categorical values
sales["location_id"] = sales["location_id"].fillna(
    sales["location_id"].mode()[0]
)

sales["sale_channel"] = sales["sale_channel"].fillna(
    sales["sale_channel"].mode()[0]
)

sales["payment_mode"] = sales["payment_mode"].fillna(
    sales["payment_mode"].mode()[0]
)

sales["salesperson_id"] = sales["salesperson_id"].fillna(
    sales["salesperson_id"].mode()[0]
)

# Fill missing numeric values
sales["discount_pct"] = sales["discount_pct"].fillna(
    sales["discount_pct"].median()
)

sales["discount_amount"] = sales["discount_amount"].fillna(
    sales["discount_amount"].median()
)

# Fix numeric datatypes
numeric_cols = [
    "units_sold",
    "unit_price",
    "total_revenue",
    "discount_pct",
    "discount_amount",
    "net_revenue"
]

for col in numeric_cols:
    sales[col] = pd.to_numeric(sales[col], errors="coerce")

# =====================================
# DIM CUSTOMER
# =====================================

customer["customer_name"] = customer["customer_name"].fillna(
    "Unknown Customer"
)

# =====================================
# DIM VEHICLE
# =====================================

vehicle["fuel_type"] = vehicle["fuel_type"].fillna(
    vehicle["fuel_type"].mode()[0]
)

# =====================================
# DIM DATE
# =====================================

date_dim["sale_date"] = pd.to_datetime(date_dim["sale_date"])

# =====================================
# SAVE CLEANED FILE
# =====================================

with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    sales.to_excel(writer, sheet_name="fact_sales", index=False)
    customer.to_excel(writer, sheet_name="dim_customer", index=False)
    vehicle.to_excel(writer, sheet_name="dim_vehicle", index=False)
    location.to_excel(writer, sheet_name="dim_location", index=False)
    date_dim.to_excel(writer, sheet_name="dim_date", index=False)

print("Data cleaned successfully!")
print("Saved as:", OUTPUT_FILE)





import pandas as pd

file_path = "vehicle_sales_tables.csv.xlsx"

# Load Excel file
xls = pd.ExcelFile(file_path)

# Show sheet names
print("Sheets in workbook:")
print(xls.sheet_names)

# Display all rows and columns
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# Read and display each sheet
for sheet in xls.sheet_names:
    print("\n" + "="*50)
    print(f"SHEET: {sheet}")
    print("="*50)

    df = pd.read_excel(file_path, sheet_name=sheet)

    print(df)
    print("\nShape:", df.shape)




#connecting to sql


import pandas as pd
from sqlalchemy import create_engine

# MySQL Connection
user = "root"
password = "Smart@1408"
host = "localhost"
port = 3306
database = "vehicle_sales_db"

engine = create_engine(
    f"mysql+pymysql://{user}:{password.replace('@', '%40')}@{host}:{port}/{database}"
)

print("Connected Successfully!")



file_path = "vehicle_sales_tables.csv.xlsx"

sales = pd.read_excel(file_path, sheet_name="fact_sales")
customer = pd.read_excel(file_path, sheet_name="dim_customer")
vehicle = pd.read_excel(file_path, sheet_name="dim_vehicle")
location = pd.read_excel(file_path, sheet_name="dim_location")
date_dim = pd.read_excel(file_path, sheet_name="dim_date")


sales.to_sql(
    "fact_sales",
    con=engine,
    if_exists="replace",
    index=False
)

customer.to_sql(
    "dim_customer",
    con=engine,
    if_exists="replace",
    index=False
)

vehicle.to_sql(
    "dim_vehicle",
    con=engine,
    if_exists="replace",
    index=False
)

location.to_sql(
    "dim_location",
    con=engine,
    if_exists="replace",
    index=False
)

date_dim.to_sql(
    "dim_date",
    con=engine,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully!")



query = "SELECT * FROM fact_sales LIMIT 5"

df = pd.read_sql(query, engine)

print(df)   
