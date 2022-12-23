FROM confluentinc/cp-kafka-connect:7.3.0

ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"

RUN confluent-hub install --no-prompt snowflakeinc/snowflake-kafka-connector:1.5.5 &&\
  confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.2.2 &&\
  confluent-hub install --no-prompt confluentinc/kafka-connect-json-schema-converter:7.3.0
