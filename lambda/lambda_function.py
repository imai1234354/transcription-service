import json
import boto3

def lambda_handler(event, context):
    # S3バケットとオブジェクトキーを取得
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Amazon Transcribeクライアントを作成
    transcribe = boto3.client('transcribe')
    
    # トランスクリプションジョブの名前を作成
    job_name = key.split('.')[0]
    
    # 音声ファイルのS3 URIを作成
    job_uri = f's3://{bucket}/{key}'
    
    # トランスクリプションジョブを開始
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat=key.split('.')[-1],
        LanguageCode='en-US',
        OutputBucketName=bucket,
        OutputKey=f'transcriptions/{job_name}.json'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Transcription job started successfully')
    }
