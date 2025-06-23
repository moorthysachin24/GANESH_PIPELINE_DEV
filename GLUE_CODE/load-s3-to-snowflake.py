import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1750489236990 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://ganesh-s3-inbound-datafiles"], "recurse": True}, transformation_ctx="AmazonS3_node1750489236990")

# Script generated for node Snowflake
Snowflake_node1750489242514 = glueContext.write_dynamic_frame.from_options(frame=AmazonS3_node1750489236990, connection_type="snowflake", connection_options={"autopushdown": "on", "dbtable": "emp_details", "connectionName": "Snowflake_connection", "preactions": "CREATE TABLE IF NOT EXISTS public.emp_details (FIRST_NAME string, LAST_NAME string, EMAIL string);", "sfDatabase": "demo_db", "sfSchema": "public"}, transformation_ctx="Snowflake_node1750489242514")

job.commit()