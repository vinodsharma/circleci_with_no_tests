FROM amazonlinux:2017.03

ENV VENV_DIR=/venv

RUN yum update -y
RUN yum -y groupinstall "Development Tools"
RUN yum -y install zlib-devel openssl-devel wget \ 
  gcc-c++ atlas-sse3-devel lapack-devel zip\
  postgresql-devel mysql-devel docker
RUN wget https://github.com/openssl/openssl/archive/OpenSSL_1_0_2l.tar.gz \
  && tar -zxvf OpenSSL_1_0_2l.tar.gz \
  && cd openssl-OpenSSL_1_0_2l/ \
  && ./config shared \
  && make \
  && make install \
  && export LD_LIBRARY_PATH=/usr/local/ssl/lib/ \
  && cd .. \
  && rm OpenSSL_1_0_2l.tar.gz \
  && rm -rf openssl-OpenSSL_1_0_2l/ \
  && wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz \
  && tar xJf Python-3.6.0.tar.xz \
  && cd Python-3.6.0 \
  && ./configure \
  && make \
  && make install \
  && cd .. \
  && rm Python-3.6.0.tar.xz \
  && rm -rf Python-3.6.0 \
  && pip3.6 install -U virtualenv \
  && virtualenv -p python3 $VENV_DIR \
  && source $VENV_DIR/bin/activate \
  && pip install --upgrade --no-cache-dir sqlalchemy \
  && pip install --upgrade --no-cache-dir psycopg2 \
  && pip install --upgrade --no-cache-dir python-dotenv \
  && pip install --upgrade --no-cache-dir awscli \
  && pip install --upgrade --no-cache-dir boto3 \
  && pip install --upgrade --no-cache-dir pytest
