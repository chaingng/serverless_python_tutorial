import datetime
import gspread
import boto3
import pytz
from oauth2client.service_account import ServiceAccountCredentials
from slackclient import SlackClient
import os
import pdb


def notify_to_slack(message, channel='#kpi'):
    slack_token = os.environ.get('SERVERLESS_SLACK_BOT_API_TOKEN')
    sc = SlackClient(slack_token)
    sc.api_call(
        "chat.postMessage",
        channel=channel,
        as_user=True,
        text=message
    )


def get_kpi():
    client = boto3.client(
        'dynamodb',
        aws_access_key_id=os.environ.get('SERVERLESS_AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('SERVERLESS_AWS_SECRERT_KEY'),
        region_name='ap-northeast-1'
    )

    entry_num = client.describe_table(TableName='serverless_blog_entries')[
        'Table']['ItemCount']
    return entry_num


def update_gas(today, entry_num):
    keyfile_path = 'serverless-gas-client-secret.json'
    scope = ['https://spreadsheets.google.com/feeds']
    doc_id = '1Loagi0Bxr5OL4SdW_KkpKYtat4jIFYV-PTVU5o8cjZQ'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        keyfile_path, scope)

    client = gspread.authorize(credentials)

    gfile = client.open_by_key(doc_id)
    worksheet = gfile.sheet1

    list_of_lists = worksheet.get_all_values()
    new_row_number = len(list_of_lists) + 1

    worksheet.update_cell(new_row_number, 1, today)
    worksheet.update_cell(new_row_number, 2, entry_num)


def run_bot():
    today = str(datetime.datetime.now(pytz.timezone('Asia/Tokyo')).date())
    entry_num = get_kpi()
    update_gas(today, entry_num)

    message = '{}\n記事数:{}\nhttps://docs.google.com/spreadsheets/d/1Loagi0Bxr5OL4SdW_KkpKYtat4jIFYV-PTVU5o8cjZQ'.format(
        today, entry_num)
    notify_to_slack(message)


if __name__ == "__main__":
    run_bot()
