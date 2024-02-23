import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from beam_nuggets.io.kafkaio import KafkaConsume
import json
import psycopg2


class ExtractAndTransform(beam.DoFn):
    def process(self, element):
        _, value = element
        transaction = json.loads(value)
        print(f"Read from Kafka: {transaction}")
        yield transaction


class WriteToPostgres(beam.DoFn):
    def __init__(self, connection_options):
        self.connection_options = connection_options

    def start_bundle(self):
        self.conn = psycopg2.connect(**self.connection_options)

    def finish_bundle(self):
        self.conn.close()

    def process(self, element):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO financial_transactions (
                    transaction_id, product_id, product_name, product_category,
                    product_price, product_quantity, product_brand, currency,
                    customer_id, transaction_date, payment_method, total_amount
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
                (
                    element["transactionId"],
                    element["productId"],
                    element["productName"],
                    element["productCategory"],
                    element["productPrice"],
                    element["productQuantity"],
                    element["productBrand"],
                    element["currency"],
                    element["customerId"],
                    element["transactionDate"],
                    element["paymentMethod"],
                    element["totalAmount"],
                ),
            )
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()


def run():
    options = PipelineOptions()
    p = beam.Pipeline(options=options)

    consumer_config = {
        "topic": "financial_transactions",
        "bootstrap_servers": "localhost:9092",
        "group_id": "beam-consumer-group",
    }

    connection_options = {
        "host": "localhost",
        "port": "5432",
        "database": "postgres",
        "user": "postgres",
        "password": "postgres",
    }

    (
        p
        | "ReadFromKafka"
        >> KafkaConsume(
            consumer_config=consumer_config,
        )
        | "ExtractAndTransform" >> beam.ParDo(ExtractAndTransform())
        | "WriteToPostgres" >> beam.ParDo(WriteToPostgres(connection_options))
    )

    result = p.run()
    result.wait_until_finish()


if __name__ == "__main__":
    run()
