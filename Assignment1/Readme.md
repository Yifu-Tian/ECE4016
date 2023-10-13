## Abstract
- This assignment implemented a local DNS serve, which is used to fetch back the IP address as the client required. Here are two ways to access, ask public server for IP address and search iteratively.
- ![image](https://github.com/Yifu-Tian/ECE4016/assets/102942951/f577ff7d-485b-4cd8-b57a-cddfc44eda24)

## HOW TO EXECUTE
- Firstly, enter "python3 DNS.py" in the terminal(under the folder that contains DNS.py)
- Secondly, it will ask you to enter a flag (0 or 1) to determine which method to be used
- After you enter the flag value, open another terminal and enter "dig <website> @127.0.0.1 -p1234" to send queries to local DNS sever, replace the <website> with any website you want. e.g."www.baidu.com", "www.example.com"

## RESULT
- Enter flag = 0
It will ask the public server for the IP answer and return
- Enter flag = 1
If cache hit, return the result directly;
If cache miss, it will do iterative query by asking the root server, then ask next authority DNS based on the answer provided by the root server. It will print out all IP addresses it has passed after getting result. Finally, store the data into the cache so that it can be faster to fetch back if next time you ask the same domain name.

## NOTE: TIMEOUT OCCURS
- Sometimes the timeout occurs and the terminals give no response. The only solution is to close all terminals and try again.
