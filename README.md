# CrimesDatabaseAWS
To run the application, you will need to configure the following - 

1. VPC connection-
* Created a VPC with CIDR of 10.0.0.0/16. I don't really need to create another VPC, but I want to avoid any problems with prior configurations.
* Created a Subnet in the VPC with CIDR of 10.0.0.0/24.
* Created an Internet Gateway and attached it to the VPC.
* Edited the default Route Table to send 0.0.0.0/0 traffic to the Internet Gateway. (I'm only creating a public subnet, so don't need a route table for private subnet.)
* Created a Redshift Cluster Subnet Group with the single subnet I created.

2. Redshift Cluster -
* Launch a 1-node Redshift cluster into the Cluster Subnet Group. Publicly accessible = Yes, default Security Group.
* Go back to the VPC console to edit the Default Security Group. Added an Inbound rule for Redshift from Anywhere.
* Waited for the Cluster to become ready.

3. IAM -
* Attach IAM Roles for S3FullAccess in Redshift, Lambda.

4. Lambda -
* Upload zipped project to create a lambda function.
* Test the function to trigger the application
