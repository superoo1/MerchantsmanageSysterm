FROM ubuntu:16.04

#用ubuntu国内源替换默认源
RUN rm /etc/apt/sources.list
COPY sources.list /etc/apt/sources.list
Copy  ./MerchantsmanageSysterm  /opt/MerchantsmanageSysterm
WORKDIR /opt/MerchantsmanageSysterm/MerchantsmanageSysterm


#安装python3.6必要的包。源镜像太精简了，ip ifconfig之类的都没有。后续安装python pip也需要一些。但是build_essential似乎不必须，先去了。如果后面安装numpy之类需要gcc了，再加上
RUN apt-get update
#RUN apt-get install -y apt-transport-https vim iproute2 net-tools build-essential ca-certificates curl wget software-properties-common
RUN apt-get install -y apt-transport-https vim iproute2 net-tools ca-certificates curl wget software-properties-common
RUN  apt-get install -y libmysqlclient-dev &&  apt-get install -y build-essential
RUN apt-get install -y inetutils-ping &&  apt-get install -y net-tools
#安装python3.6 来自第三方
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y python3.6
RUN apt install -y python3.6-dev
RUN apt install -y python3.6-venv
#为3.6安装pip
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN  apt-get install -y nginx;
RUN nginx -t
#和自带的3.5共存
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
RUN update-alternatives --config python3
RUN pwd
RUN ls /opt/MerchantsmanageSysterm/MerchantsmanageSysterm
RUN  pip install --upgrade pip
RUN   pip install -r requirments.txt
#print()时在控制台正常显示中文


ENTRYPOINT [ "python3","initsystem.py" ]


ENV PYTHONIOENCODING=utf-8


