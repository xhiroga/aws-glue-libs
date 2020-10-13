from datetime import datetime
import sys
import boto3
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

s3 = boto3.resource("s3")
sc = SparkContext()

print("Hello Glue!")
