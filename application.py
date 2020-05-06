from redshift_utils import Messages
from redshift_utils import ScriptReader
from redshift_utils import RedshiftDataManager
from settings import DB_CONNECTION
from settings import SCRIPT_PATH
from settings import SCHEMA_PATH
from loading import LoadData
from datetime import datetime
import boto3

class Exec(object):
    
    def load(self):
        print(SCHEMA_PATH)
        schema = ScriptReader.get_script(SCHEMA_PATH)
        r = RedshiftDataManager.run_query(schema, DB_CONNECTION)
        copy_data = LoadData()
        copy_data.loadstates()
        copy_data.loadgunviolence()
        copy_data.loadhatecrimes()
    
    def execute(self):
        for i in range(1,5):
            script = ScriptReader.get_script(SCRIPT_PATH[str(i)])
            r = RedshiftDataManager.run_query(script, DB_CONNECTION)
        
            bucket_name = "crimeanalysisyk"
            file_name = "result"+str(datetime.now())+".txt"
            lambda_path = "/tmp/" + file_name
            s3_path = "output/" + file_name
        
            s3 = boto3.resource("s3")
            s3.Bucket(bucket_name).put_object(Key=s3_path, Body=(bytes(r.encode('UTF-8'))),ServerSideEncryption='AES256')
        return RedshiftDataManager.run_query(script, DB_CONNECTION)