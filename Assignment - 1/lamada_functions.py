//version - 1

import json
import base64, csv, io
from statistics import mean


def lambda_handler(event, context):
   if event['httpMethod'] == 'GET':
       val = event['queryStringParameters']['key']
       return {
       'statusCode': 200,
       'body': json.dumps(f"YOUR_SRN: {val}")
       }


   elif event['httpMethod'] == 'POST':
       base64csv = event["body"]
       if base64csv == None:
           return {
           'statusCode': 200,
           'body': json.dumps("No CSV found.")
           }   
          
       rows = []
       decrypted = base64.b64decode(str(base64csv)).decode('utf-8')
      
       with io.StringIO(decrypted) as fp:
           reader = list(csv.reader(fp, delimiter=",", quotechar='"'))
           for row in reader[4:-2]:
               rows.append(row)
      
       transposed = [list(i) for i in zip(*rows)]
      
       avg = dict()
       for person_times in transposed:
           person = person_times[0]
           times = [float(time) for time in person_times[1:]]
          
           avg[person] = mean(times)
          
       return {
           'statusCode': 200,
           'body': json.dumps(str(avg))
       }
  
   else:
       return {
          'statusCode': 200,
          'body': json.dumps("Only GET and POST are supported")
       }
       
//version - 2
import json
import base64, csv, io
from statistics import mean

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        val = event['queryStringParameters']['key']
        return {
            'statusCode': 200,
            'body': json.dumps(f"YOUR_SRN: {val}"),
            'headers': {'Content-Type': 'application/json'}
        }

    elif event['httpMethod'] == 'POST':
        base64csv = event["body"]
        if not base64csv:
            return {
                'statusCode': 200,
                'body': json.dumps("No CSV found."),
                'headers': {'Content-Type': 'application/json'}
            }   

        rows = []
        decrypted = base64.b64decode(base64csv).decode('utf-8')

        with io.StringIO(decrypted) as fp:
            reader = list(csv.reader(fp, delimiter=",", quotechar='"'))
            for row in reader[4:-2]:
                rows.append(row)

        transposed = [list(i) for i in zip(*rows)]

        avg = dict()
        for person_times in transposed:
            person = person_times[0]
            times = [float(time) for time in person_times[1:]]

            avg[person] = mean(times)

        return {
            'statusCode': 200,
            'body': json.dumps(str(avg)),
            'headers': {'Content-Type': 'application/json'}
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps("Only GET and POST are supported"),
            'headers': {'Content-Type': 'application/json'}
        }

