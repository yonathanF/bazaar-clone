FROM grahamdumpleton/mod-wsgi-docker:python-3.5
RUN apt-get update && \
	apt-get install -y --no-install-recommends \
		git \
		python3-pip \
		python3-dev \
		libmysqlclient-dev \
		unattended-upgrades && \
	rm -r /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENV LANG=en_US.UTF-8 PYTHONHASHSEED=random \ PATH=/usr/local/python/bin:/usr/local/apache/bin:$PATH \ MOD_WSGI_USER=www-data MOD_WSGI_GROUP=www-data
