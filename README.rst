================
command-notifier
================

A very simple command-notification package based on SQS for distributed systems

> Warning: This can be abused to take down your entire infrastructure, gain root access, etc.

Installation
============

Using PIP via PyPI::

    pip install command-notifier

Using PIP via Github::

    pip install git+git://github.com/josegonzalez/python-command-notifier.git#egg=command-notifier

Usage
=====

CLI Usage of cn-subscribe is as follows::

    usage: cn-subscribe [-h] [-a AWS_ACCESS_KEY_ID] [-s AWS_SECRET_ACCESS_KEY]
                        [-r EC2_REGION] [-t SNS_TOPIC] [-w SNS_WAIT_TIME_SECONDS]
                        [-q SQS_QUEUE]

    cn-subscribe, a tool to run commands published from sqs

    optional arguments:
      -h, --help            show this help message and exit
      -a AWS_ACCESS_KEY_ID, --aws-access-key-id AWS_ACCESS_KEY_ID
                            AWS Access Key ID
      -s AWS_SECRET_ACCESS_KEY, --aws-secret-access-key AWS_SECRET_ACCESS_KEY
                            AWS Secret Access Key
      -r EC2_REGION, --ec2-region EC2_REGION
                            EC2 Region
      -t SNS_TOPIC, --sns-topic SNS_TOPIC
                            SNS Topic to subscribe to
      -w SNS_WAIT_TIME_SECONDS, --sns-wait-time-seconds SNS_WAIT_TIME_SECONDS
                            SNS Wait Time in Seconds
      -q SQS_QUEUE, --sqs-queue SQS_QUEUE
                            SQS Queue to utilize to

    cn-subscribe is pwnage

CLI Usage of cn-publish is as follows::

    usage: cn-publish [-h] [-a AWS_ACCESS_KEY_ID] [-s AWS_SECRET_ACCESS_KEY]
                      [-c COMMAND] [-r EC2_REGION] [-t SNS_TOPIC]

    cn-publish, a tool to publish a command via sns

    optional arguments:
      -h, --help            show this help message and exit
      -a AWS_ACCESS_KEY_ID, --aws-access-key-id AWS_ACCESS_KEY_ID
                            AWS Access Key ID
      -s AWS_SECRET_ACCESS_KEY, --aws-secret-access-key AWS_SECRET_ACCESS_KEY
                            AWS Secret Access Key
      -c COMMAND, --command COMMAND
                            Command to publish
      -r EC2_REGION, --ec2-region EC2_REGION
                            EC2 Region
      -t SNS_TOPIC, --sns-topic SNS_TOPIC
                            SNS Topic to publish to

    cn-publish is pwnage

You can also use the equivalent environment variables in place of command arguments.

