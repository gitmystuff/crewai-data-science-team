# Data Engineering Pipeline Log

## 1. Data Collection
- Successfully used the Iris Data Fetcher tool to download the raw Iris dataset
- Raw data saved as 'iris_data.csv' in the local repository
- Data is now available for the team to use in subsequent processing steps

## 2. Data Cleaning Process Documentation
The following steps should be implemented in the data cleaning phase:

1. **Data Validation**
   - Check for missing values in all columns (sepal_length, sepal_width, petal_length, petal_width, species)
   - Verify data types for each column (numerical for measurements, categorical for species)
   - Identify and handle any outliers using statistical methods (e.g., z-score or IQR)

2. **Data Transformation**
   - Convert species names to a standardized format (lowercase, remove extra spaces)
   - Create species_id mapping based on the Iris Species Metadata Table schema
   - Format column names for consistency

3. **Data Quality Checks**
   - Ensure measurement values are within realistic ranges for iris flowers
   - Validate species against the known iris species in our metadata
   - Generate data quality report with metrics (completeness, accuracy, consistency)

## 3. Data Scaling/Normalization Documentation
For machine learning model compatibility, implement the following scaling steps:

1. **Feature Scaling**
   - Apply Min-Max scaling to normalize all numeric features between 0 and 1
     ```python
     # Pseudocode for Min-Max scaling
     scaled_value = (value - min_value) / (max_value - min_value)
     ```
   - Alternatively, use StandardScaler for normal distribution (mean=0, std=1)
     ```python
     # Pseudocode for Standard scaling
     scaled_value = (value - mean) / standard_deviation
     ```

2. **Feature Engineering**
   - Calculate derived features if needed (e.g., sepal_area = sepal_length * sepal_width)
   - Create one-hot encoding for the species categorical variable

## 4. Data Storage Strategy
Based on the defined schema:

1. **Raw Data Storage**
   - Store original 'iris_data.csv' in the Raw Data Repository
   - Parse and load data into Iris Metrics Table and Iris Species Metadata Table

2. **Processed Data Storage**
   - After cleaning and scaling, store transformed data in the Processed Data Repository
   - Populate Feature Set Table with normalized values
   - Prepare structure for Classification Model Outputs and User Interaction Logs

## 5. Pipeline Reproducibility
To ensure reproducibility of the data pipeline:

1. **Version Control**
   - Track all data processing scripts in version control
   - Document data lineage from raw to processed formats

2. **Automated Pipeline**
   - Implement automated workflow for:
     - Data fetching (using Iris Data Fetcher)
     - Cleaning and validation
     - Scaling and normalization
     - Loading into appropriate database tables

3. **Logging**
   - Implement comprehensive logging of all pipeline steps
   - Record data quality metrics at each stage

The iris_data.csv file has been successfully created and is now ready for the next steps in the pipeline process.
