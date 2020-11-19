FROM phusion/baseimage:focal-1.0.0-alpha1-amd64

# code and dir
RUN mkdir /mymdb
WORKDIR /mymdb
COPY requirements* /mymdb/
COPY core/ /mymdb
COPY templates/ /mymdb
COPY user/ /mymdb
COPY main/ /mymdb
COPY manage* /mymdb
COPY scripts/ /mymdb/scripts
RUN mkdir /var/log/mymdb/
RUN touch /var/log/mymdb/mymdb.log

# Installing needed packages
RUN apt-get -y update
RUN apt-get install -y nginx postgresql-client python3 python3-pip
RUN pip3 install virtualenv
RUN virtualenv /mymdb/venv
RUN bash /mymdb/scripts/pip_install.sh /mymdb

# Collect the static files
RUN bash /mymdb/scripts/collect_static.sh /mymdb

# Add nginx
COPY nginx/mymdb.conf /etc/nginx/sites-available/mymdb.conf
RUN rm /etc/nginx/site-enabled/*
RUN ln -s /etc/nginx/sites-available/mymdb.conf /etc/nginx/sites-enabled/mymdb.conf
COPY runit/nginx /etc/service/nginx
RUN chmod +x /etc/service/nginx/run

# clean up and document the port 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80