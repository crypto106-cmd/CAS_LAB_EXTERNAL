# Q4: Analyze Server Requests
# Algorithm: Single pass with hash map counting
# Time Complexity: O(n) | Space Complexity: O(k) where k = unique IPs

def analyze_server_requests():
    """
    Analyze server logs to find:
    1. The most active IP address (ties broken by lexicographic order)
    2. Total number of 4xx responses
    3. Total number of 5xx responses
    """
    # Read the number of log entries
    n = int(input())
    
    # Dictionary to count requests per IP
    ip_count = {}
    
    # Counters for 4xx and 5xx responses
    count_4xx = 0
    count_5xx = 0
    
    # Process each log entry
    for i in range(n):
        parts = input().split()
        ip_address = parts[0]
        status_code = int(parts[1])
        
        # Count requests per IP
        if ip_address in ip_count:
            ip_count[ip_address] += 1
        else:
            ip_count[ip_address] = 1
        
        # Count 4xx responses (status codes 400-499)
        if 400 <= status_code <= 499:
            count_4xx += 1
        
        # Count 5xx responses (status codes 500-599)
        elif 500 <= status_code <= 599:
            count_5xx += 1
    
    # Find the most active IP
    # On tie, choose lexicographically smallest IP
    most_active_ip = None
    max_requests = 0
    
    for ip in ip_count:
        requests = ip_count[ip]
        # Update if this IP has more requests, or same requests but smaller IP
        if requests > max_requests:
            max_requests = requests
            most_active_ip = ip
        elif requests == max_requests:
            if ip < most_active_ip:
                most_active_ip = ip
    
    # Print results
    print(most_active_ip)
    print(count_4xx)
    print(count_5xx)


# ---- Main Program ----
analyze_server_requests()
