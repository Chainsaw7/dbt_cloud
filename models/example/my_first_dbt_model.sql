
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}
    
with CTE as (
    select * from {{ source('staging', 'products') }} 
    where price<30.0
)
select *
from CTE

