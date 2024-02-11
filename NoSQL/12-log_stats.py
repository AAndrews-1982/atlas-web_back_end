#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

def nginx_logs_stats():
    """Function to print stats about Nginx logs."""
    client = MongoClient('mongodb://127.0.0.1:27017/')
    nginx_collection = client.logs.nginx
    
    # Total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\t{method}: {count}")
    
    # GET /status
    get_status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{get_status_count} documents with method=GET path=/status")

if __name__ == "__main__":
    nginx_logs_stats()

