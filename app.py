from flask import Flask, request, render_template, jsonify
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_temp_creds', methods=['POST'])
def generate_temp_creds():
    data = request.json
    access_key = data.get('access_key')
    secret_key = data.get('secret_key')
    role_arn = data.get('role_arn')

    if not access_key or not secret_key or not role_arn:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        sts_client = boto3.client(
            'sts',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name='us-east-1'  # Change if needed
        )

        response = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName='TempSession'
        )

        creds = response['Credentials']
        return jsonify({
            'AccessKeyId': creds['AccessKeyId'],
            'SecretAccessKey': creds['SecretAccessKey'],
            'SessionToken': creds['SessionToken'],
            'Expiration': creds['Expiration'].isoformat()
        })

    except ClientError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


    