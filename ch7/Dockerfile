FROM confluentinc/cp-kafka-connect-base:6.2.0

ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"

ARG CONNECTOR_NAME
ARG CONNECTOR_VERSION
RUN confluent-hub install --no-prompt confluentinc/${CONNECTOR_NAME}:${CONNECTOR_VERSION}
RUN curl -k -SL "http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.37.tar.gz" \
    | tar -xzf - -C /usr/share/confluent-hub-components/confluentinc-kafka-connect-jdbc/lib \
    --strip-components=1 mysql-connector-java-5.1.37/mysql-connector-java-5.1.37-bin.jar
