# manage-snapshot-AWS
Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage
AWS EC2 instance snapshots.

## Configuring

manage-ec2 uses configruation file created by the AWS cli. e.g.

`aws configure --profile manage-ec2`

## Running

`pipenv run python manage-ec2/manage-ec2.py <command>
<--project=PORJECT>`

*command* is list, start, or stop
*project* is optional