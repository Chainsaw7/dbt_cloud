import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def model(dbt, session: snowpark.Session): 
    # Your code goes here, inside the "main" handler.
    dataframe1 = dbt.source("staging", "products")  
    dataframe2 = dbt.source("staging", "orders")  
    # Print a sample of the dataframe to standard output.
    
    df1 = dataframe1.join(dataframe2, how="inner", on="product_id" )
    
    df1 = df1.withColumn("revenue", df1["price"] * df1["quantity"])
    df2=df1[['product_id', 'revenue' ]]

    df3 = df2.groupBy("product_id").agg({"revenue": "sum"})
    # Return value will appear in the Results tab.
    return df3
