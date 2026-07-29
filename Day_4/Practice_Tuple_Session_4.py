# Tuple of locations as (Latitude, Longitude)
locations = (
    (35.6892, 51.3890),  # Tehran
    (38.07431, 46.28709),  # Tabriz Shahnaz
    (29.5918, 52.5837),  # Shiraz
    (38.0743145, 46.2870879),  # Tabriz Shah-Gouli
    (32.6546, 51.6680)   # Isfahan
)

# Tabriz geographic bounding box
LAT_MIN, LAT_MAX = 38.00, 38.15
LON_MIN, LON_MAX = 46.20, 46.40

print("### Location Check ###")

# Iterate over coordinates using tuple unpacking
for lat, lon in locations:
    # Check if coordinates fall in Tabriz boundaries
    if LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX:
        print(f"You have a location from Tabriz in your data: ({lat}, {lon})")