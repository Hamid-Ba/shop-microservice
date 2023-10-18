from redis_om import get_redis_connection


redis = get_redis_connection(host="redis-15654.c300.eu-central-1-1.ec2.cloud.redislabs.com",
                             port=15654,
                             password="dg4yUMnZvta4giaJatovD5DWlkcRnX5Y",
                             decode_responses=True)