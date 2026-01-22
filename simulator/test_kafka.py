from kafka import KafkaProducer
import os
from dotenv import load_dotenv

load_dotenv()
bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")  # Thay đổi ở đây

try:
    producer = KafkaProducer(
        bootstrap_servers=[bootstrap_servers],
        retries=0,  # Thêm để tránh retry loop nếu lỗi
        request_timeout_ms=5000  # Timeout 5s để test nhanh
    )
    print("✅ Kết nối Kafka thành công!")
    producer.close()
except Exception as e:
    print(f"❌ Lỗi kết nối: {e}")