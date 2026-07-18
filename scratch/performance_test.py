import time
import requests

API_URL = "http://localhost:8000/api/v1/supply-chain/dashboard/network"

def run_performance_test():
    print(f"Testing caching performance on {API_URL}")
    print("-" * 50)
    
    # Warm up / Cache Miss
    start_time = time.time()
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Backend server is not running at localhost:8000. Start it with uvicorn app.main:app --reload")
        return
        
    miss_time = (time.time() - start_time) * 1000
    print(f"Request 1 (Likely Cache Miss): {miss_time:.2f} ms")
    
    # Cache Hits
    hit_times = []
    for i in range(2, 6):
        start_time = time.time()
        requests.get(API_URL)
        hit_time = (time.time() - start_time) * 1000
        hit_times.append(hit_time)
        print(f"Request {i} (Likely Cache Hit): {hit_time:.2f} ms")
        
    avg_hit = sum(hit_times) / len(hit_times)
    print("-" * 50)
    print(f"Average Cache Hit Latency: {avg_hit:.2f} ms")
    
    if avg_hit < miss_time:
        improvement = (miss_time - avg_hit) / miss_time * 100
        print(f"Performance Improvement: {improvement:.2f}% faster due to Redis Caching!")
    else:
        print("No significant improvement detected. Cache might be disabled or DB queries are incredibly fast.")

if __name__ == "__main__":
    run_performance_test()
