## https://serper.dev/

from dotenv import load_dotenv
load_dotenv()
import os

# # os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# serper_api_key = os.getenv('SERP_API_KEY')
# if serper_api_key is None:
#     raise ValueError("SERP_API_KEY is not set in the environment!")

from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()