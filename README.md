# Leave Management System
This Project helps applying and approving leaves in an organization. There are two roles defined, Employee and Manager. Where leaves applied by employee are Approved/Reject with a comment by Manager. Employee can cancel his/her own pending leaves them self. Total number of leaves an employee can Utilize are 21.

## Getting Started
Development deployment of this project is running @ http://surighanta.in:8000/ to get familiar with the project.

### Prerequisites
Install python3, pip3, python’s set-up tools.

Example:
yum install python3-devel
yum install mysqlclient
yum install gcc

wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
sudo yum localinstall mysql80-community-release-el7-3.noarch.rpm
sudo yum install mysql-community-server

Install independent python libraries using the dependencies listed in the dependencies file.
Install, Start and initialize database in below described structure:

mysql> SELECT DATABASE();
+------------+
| DATABASE() |
+------------+
| lms        |
+------------+

mysql> SHOW TABLES;
+---------------+
| Tables_in_lms |
+---------------+
| leaves        |
| users         |
+---------------+

mysql> DESCRIBE users;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| userid   | varchar(20) | NO   | PRI | NULL    |       |
| password | varchar(30) | NO   |     | NULL    |       |
| name     | varchar(20) | NO   |     | NULL    |       |
| role     | varchar(20) | NO   |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+

mysql> DESCRIBE leaves;
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| leaveid      | varchar(20) | NO   | PRI | NULL    |       |
| userid       | varchar(20) | NO   |     | NULL    |       |
| applydate    | varchar(30) | NO   |     | NULL    |       |
| leavedate    | varchar(30) | NO   |     | NULL    |       |
| nodays       | int(30)     | NO   |     | NULL    |       |
| status       | varchar(20) | NO   |     | NULL    |       |
| approvedby   | varchar(30) | YES  |     | NULL    |       |
| approveddate | varchar(30) | YES  |     | NULL    |       |
| comment      | varchar(30) | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+

After the installation is completed, export the App path and start the application:

export FLASK_APP=main.py
flask run --port=8000 --host=0.0.0.0 &

## Deployment
This application can be installed any system where python and mysql database can work.

## Authors
Suresh Ganta (suresh.komarada@gmail.com)
