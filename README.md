# 音声認識によるトランスクリプションサービス

このプロジェクトは、AWSサービスを使用して音声ファイルをアップロードすると、自動で文字起こしを行うサービスです。

## 使用技術

- AWS Lambda
- Amazon Transcribe
- Amazon S3
- API Gateway
- AWS Amplify


## セットアップ手順

1. リポジトリをクローンします:
    ```
    git clone <リポジトリURL>
    cd transcription-service
    ```

2. Lambda関数のデプロイ:
    - AWS Lambdaコンソールで新しい関数を作成します。
    - `lambda_function.py`のコードを関数にコピーします。
    - `boto3`ライブラリを含むLambdaレイヤーを作成して関数にアタッチします。

3. S3バケットの作成:
    - S3バケットを作成し、`lambda_function.py`のコード内で指定します。

4. API Gatewayの設定:
    - API Gatewayで新しいAPIを作成し、Lambda関数をトリガーするエンドポイントを設定します。

5. Amplifyプロジェクトの初期化およびデプロイ:
    ```
    cd amplify
    amplify init
    amplify add storage
    amplify add api
    amplify push
    ```

6. Reactアプリケーションを起動:
    ```
    npm install
    npm start
    ```

## 使用方法

- 音声ファイルをアップロードすると、Lambda関数がトランスクリプションジョブを開始します。
- トランスクリプションが完了すると、結果がS3に保存されます。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。



