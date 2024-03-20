import pandas as pd

# Define a mapping from the given ArcGIS fields to the ICPR table fields based on the image provided by the user.
field_mapping = {
    'ET_ID': 'ID',           # Assuming ET_ID corresponds to the unique ID for ICPR
    'NAME': 'Name',          # Basin name
    'NODE': 'Node',          # Associated node
    'TC': 'TimeOfConcentration', # Time of concentration
    # 'AREA_ACRES': None,    # Area in acres is not mapped directly; may need to be calculated or formatted
    # Additional fields that are required by the ICPR model should be added here.
    # Fields that are not needed are commented out or not included in the mapping.
}

# Load the sample data from the provided CSV file
sample_data_path = '/path/to/your/sampledatatable.csv'
sample_data = pd.read_csv(sample_data_path)

# Apply the field mapping to rename the columns
icpr_data = sample_data.rename(columns=field_mapping)

# Keep only the columns that are needed for the ICPR model
icpr_data = icpr_data[list(field_mapping.values())]

# Convert Time of Concentration to integer if necessary (assuming it should be an integer based on the placeholder 99999 in the image)
icpr_data['TimeOfConcentration'] = icpr_data['TimeOfConcentration'].astype(int)

# Display the transformed data
print(icpr_data.head())

# Save the transformed data to a new CSV file
output_path = '/path/where/you/want/to/save/icpr_transformed_data.csv'
icpr_data.to_csv(output_path, index=False)
