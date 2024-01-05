# Effective Pandas
## Pattern for Data Manipulation

### Intro
- [X] Data 

### Data Structure
- [X] Summary

### Series
- [X] Index abstraction
- [X] pandas Series
- [X] NaN value
- [X] Optional Integer Support for NaN
- [X] Similar to Numpy
- [X] Categorical Data

### Series Deep Dive
- [X] Loading the Data
- [X] Series Attributes

### Operators(& Dunder Methods)
- [X] Intro
- [X] Dunder Methods
- [X] Index Alignment
- [X] Broadcasting
- [X] Iteration
- [X] Operator Methods
- [X] Chaining

### Aggregate Methods
- [X] Aggregation
- [X] Count and Mean of an Attribute
- [X] .agg and Aggregation Strings

### Conversion Methods
- [X] Automatic Conversion
- [X] Memory Usage
- [X] String and Category Types
- [X] Ordered Categories
- [X] Converting to Other Types

### Manipulation Methods
- [X] .apply and .where
- [X] If Else
- [X] Missing Data
- [X] Filling in Missing Data
- [X] Interpolating Data
- [X] Clipping 
- [X] Sorting Value
- [X] Sorting the Index
- [X] Dropping Duplicates
- [X] Ranking Data
- [X] Replacing Data
- [X] Binning

### Indexing Operations
- [X] Prepping the Data and Renaming the index
- [X] Resetting the index
- [X] .loc Attributes
- [X] .iloc
- [X] heads and tails
- [X] Filtering Index Values
- [X] Reindexing

### String Manipulation
- [X] String and Objects
- [X] Categorical Strings
- [X] The .str Accessor
- [X] Searching
- [X] Splitting
- [ ] Optimizing .apply with Cython
- [X] Replacing Text

### Date and Time Manipulation
- [X] Date Theory
- [X] Loading UTC Time Data
- [X] Loading Local Time Data
- [X] Local Time to UTC
- [ ] Converting to Epochs
- [X] Manipulating Dates

### Dates in the Index
- [X] Finding the missing data
- [X] filling in missing data
- [X] intepolation
- [X] dropping missing values
- [X] shifting data
- [X] rolling average
- [X] resampling
- [X] gathering aggregate values(but keeping index)
- [ ] groupby operation
- [X] cumulative operations

### Plotting with a Series
- [X] Plotting in jupyter
- [X] .plot 
- [X] histogram
- [X] box
- [X] kde
- [X] line
- [X] line plot with multiple aggregations
- [X] bar
- [X] pie
- [ ] styling

### Categorical Manipulation
- [ ] Categorical data
- [ ] Frequency Counts
- [ ] benefits of categories
- [ ] conversion to Ordinal categories
- [ ] .cat accessor
- [ ] category gotchas
- [ ] generalization

### Dataframes
- [ ] database and spreedsheet analogues
- [ ] simple python version
- [ ] Dataframes
- [ ] Construction
- [ ] Dataframe Axis


### Similarities with Series and DataFrame
- [ ] getting the data
- [ ] view data

### Math Methods in DataFrames
- [ ] Index alignment
- [ ] duplicate index

### Looping and Aggregation
- [ ] for loops
- [ ] aggregaions
- [ ] .apply method

### Columns Types, .assign an Memory Usage
- [ ] Conversion methods
- [ ] memory usage

### Creating and Updating Columns
- [ ] Loading the Data
- [ ] more column cleanup

### Dealing with Missing and Duplicated Data
- [ ] Missing data
- [ ] duplicates

### Sorting Columns and Indexes
- [ ] Soring columns
- [ ] Sorting columns Order
- [ ] Setting and Sorting the index

### Filtering and Indexing Operations
- [ ] Renaming an Index
- [ ] Resetting the Index
- [ ] Dataframe Indexing, Filtering & Querying
- [ ] Indexing by Position
- [ ] Indexing 

### Plotting with DataFrames
- [ ] line plots
- [ ] bar
- [ ] scatter
- [ ] area and stacked bar
- [ ] column distributions with KDEs,Histograms and Boxplots


### Reshaping Dataframes with Dummies
- [ ] dummy columns
- [ ] undoing dummy columns

### Reshaping By Pivoting and Grouping
- [ ] Using a custom Aggregation function
- [ ] multiple aggregation
- [ ] per column aggregations
- [ ] grouping by hierarchy
- [ ] grouping with functions


### More Aggregations
- [ ] Aggregation while keeping rows
- [ ] Filtering parts of groups


### Cross-tabulation Deep Dive
- [ ] cross-tabulation
- [ ] adding margins
- [ ] normalizing results
- [ ] hierarchical columns with cross tabulations
- [ ] heatmaps

### Melting, Transpose and Stacking Data
- [ ] melting data
- [ ] Un-melting data
- [ ] Transposing data
- [ ] stacking and Unstacking
- [ ] Flattening hierarchical index and columns


### Working with TimeSeries
- [ ] loading the data
- [ ] adding timezone info
- [ ] exploring the data
- [ ] slicing ts
- [ ] missing ts data
- [ ] exploring seasonality
- [ ] resampling data
- [ ] rules with offset aliases
- [ ] combining offset aliases
- [ ] anchored offset aliases
- [ ] resampling to finger-grain frequency
- [ ] grouping a date column with pd.Grouper



### Joining Dataframes
- [ ] Adding rows to Dataframes
- [ ] Adding cols to Dataframes
- [ ] Joins
- [ ] joins indicators
- [ ] merge validations
- [ ] joining data example
- [ ] dirty devil flow and weather data
- [ ] joining data
- [ ] validating joined data
- [ ] visualization of merged data

### Exporting data
- [ ] Dirty devil data
- [ ] read and write
- [ ] create csv
- [ ] export to ecel
- [ ] feather
- [ ] sql
- [ ] json

### Styling Dataframes
- [ ] Loading the Data
- [ ] Sparklines
- [ ] .style
- [ ] Formatting
- [ ] Embedding Bar plots
- [ ] Highlighting
- [ ] Heatmap and gradients
- [ ] Captions
- [ ] css properties
- [ ] stickiness and hidding
- [ ] hiding the index


### Debugging pandas
- [ ]  Checking if Dataframe are Equal
- [ ] Debugging Chains
- [ ] Debugging Apply
- [ ] Memory Usage
- [ ] Timing Info
