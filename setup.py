from setuptools import setup

setup(
	name='SnapshotAlyzer',
	version='0.1',
	author='Saleh Hamad',
	author_email='sssxhn@gmail.com',
	description='SnapshotAlyzer is a tool to mange AWS EC2 snapshots',
	license='GPLv3+',
	packages=['manage-ec2'],
	url="https://github.com/SAELH/manage-snapshot-AWS",
	install_requires=[
		'click',
		'boto3'
	],
	Entry_Point='''
		[console_scripts]
		manage-ec2=manage-ec2.manage-ec2:cli
	''',
)	