FROM mysql:5.7.12
RUN chown -R mysql:root /var/lib/mysql/
ADD data.sql /etc/mysql/data.sql
RUN sed -i 's/MYSQL_DATABASE/feedback_db/g' /etc/mysql/data.sql
RUN cp /etc/mysql/data.sql /docker-entrypoint-initdb.d
EXPOSE 3306