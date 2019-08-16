FROM selenium/standalone-chrome-debug:latest

COPY src/ /opt/src/

COPY build.py /opt/

RUN sudo apt-get update && sudo apt-get install -y python-pip

RUN pip install selenium

#Install SQL Server drivers and dependencies for PyODBC
ADD odbcinst.txt /etc/odbcinst.ini
ADD odbcinst.txt /etc/unixODBC/odbcinst.ini
RUN sudo apt-get install -y tdsodbc unixodbc-dev
RUN sudo apt install unixodbc-bin -y
RUN sudo apt-get clean -y
RUN dpkg --search libtdsodbc.so
RUN dpkg --search libtdsS.so

RUN pip install pyodbc

WORKDIR /opt/

ARG SITE_LOGIN_USER

ENV SITE_LOGIN_USER=$SITE_LOGIN_USER

ARG SITE_LOGIN_PWD

ENV SITE_LOGIN_PWD=$SITE_LOGIN_PWD

ARG CMD_EXECUTOR

ENV CMD_EXECUTOR=$CMD_EXECUTOR

ARG DB_USERNAME

ENV DB_USERNAME=$DB_USERNAME

ARG DB_PASSWORD

ENV DB_PASSWORD=$DB_PASSWORD
