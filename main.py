from ucimlrepo import fetch_ucirepo

print("Fetching data from UCI...")
spambase = fetch_ucirepo(id=94)

X = spambase.data.features
y = spambase.data.targets

print("Data loaded successfully!")
print(f"Total rows: {X.shape[0]}")
print(f"Total columns: {X.shape[1]}")

print("\nFirst 5 rows of data:")
print(X.head())