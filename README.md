# DynamicIpUpdater

A simple little application which can be used as a DunamicDNS updater.
It relies on having an API end-point which actually updates a DNS record with your hosting provider. I have done this via API Gateway and Route 53 on AWS.

# Requirements
- API Url
- API Key
- Hosted Zone

# Instructions
- Setup API Gateway to receive a GET request (secured with an API Key)
- Use a service integration and mapping request to update Route53
- Set up a crontab to call this script whenever you like, or some other way of triggering it
