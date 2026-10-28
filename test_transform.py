
from extract import extract
from transform import transform

raw = extract()

print("\nBefore transformation:")
print(raw.head())

print("\nMissing values before transformation:")
print(raw.isnull().sum())

clean = transform(raw)

print("\nAfter transformation:")
print(clean.head())

print("\nMissing values after transformation:")
print(clean.isnull().sum())

print("\nFinal dimensions:")
print(clean.shape)
