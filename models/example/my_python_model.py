import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def model(dbt, session: snowpark.Session): 
    # Your code goes here, inside the "main" handler.
    dataframe1 = dbt.source("staging", "products")   
    dataframe2 = dbt.source("staging", "orders")  
    # Print a sample of the dataframe to standard output.
    
    result = dataframe1.join(dataframe2, how="inner", on="product_id" )

    new_result=result[['product_id', 'price','quantity']]
    new_result.show()

    # Return value will appear in the Results tab.
    return new_result
