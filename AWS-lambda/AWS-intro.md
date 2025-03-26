### **What is Serverless Architecture?**

It sounds like there are no servers, but that’s not true. The idea is that **you don’t have to manage servers**—AWS, Google, or Azure handle them for you. You just write your code, upload it, and it runs **only when needed**. No worrying about scaling, maintenance, or idle costs. It’s like renting a taxi instead of owning a car—you only pay when you use it.

### **AWS Lambda – The Star of Serverless**

AWS Lambda is one of the most popular serverless services. You write a function, upload it, and AWS runs it **only when triggered** (like an API call, file upload, or a database update). You don’t have to think about servers, CPU, or RAM—AWS handles all that. Plus, it automatically scales. If one user triggers it, it runs once; if a million users do, AWS spins up enough instances to handle it.

### **Why Bother?**
- **No Server Management** – Focus on code, not infrastructure.
- **Scalability** – It grows with demand.
- **Cost Efficiency** – Pay only when your function runs (down to milliseconds).
- **Event-Driven** – Runs on demand, like reacting to API calls, S3 uploads, database changes, etc.
    
### **When NOT to Use Lambda?**
- If your app needs **long-running processes** (Lambda has a timeout limit).
- If you need **persistent connections** (like WebSockets).
- If you run **heavy workloads** (sometimes traditional servers or containers are better).

### **Real-Life Example**
Imagine you have a photo-sharing app. When a user uploads a picture, you want to **resize it** automatically. Instead of keeping a server running 24/7, you use AWS Lambda. Every time a new photo lands in an S3 bucket, Lambda gets triggered, resizes it, and stores it back—fast, scalable, and cheap.

That’s serverless in a nutshell—no babysitting servers, just running code when you need it.


## Practical

[Link to tutorial](https://aws.amazon.com/tutorials/run-serverless-code/)

A Lambda function consists of code you provide, associated dependencies, and configuration. The configuration information you provide includes the compute resources you want to allocate (for example, memory), execution timeout, and an IAM role that AWS Lambda can assume to execute your Lambda function on your behalf.

## Doing stuff : 

1. I signed up on AWS, and I created a lamda function in the console, with using the blueprint `Hello World Python 3.0`. 
2. I went through the lambda runtime settings to check if everything is proper, like runtime dependencies n stuff.
3. To test the lambda code function works, I created a test event on the provided code.
4. I ran the test.

After running, the output and the function logs was:

```bash
Status: Succeeded
Test Event Name: HelloWorldEvent

Response:

"Hello World"

Function Logs:

START RequestId: ec1ac24e-3d88-4980-9675-7c151614ab60 Version: $LATEST

value1 = Hello World
value2 = value2
value3 = value3

END RequestId: ec1ac24e-3d88-4980-9675-7c151614ab60

REPORT RequestId: ec1ac24e-3d88-4980-9675-7c151614ab60  Duration: 1.21 ms   Billed Duration: 2 ms   Memory Size: 128 MB Max Memory Used: 31 MB
```


### **What is FaaS (Function as a Service)?**

FaaS is a fancy way of saying **“just run my function when needed”** without worrying about servers. You write small pieces of code (functions), and the cloud provider runs them **only when triggered**. It’s like ordering food when you’re hungry instead of cooking all the time—you don’t need a full-time kitchen (server), just the food (function) when you want it.

### **How is it Different from Serverless?**
FaaS is a **part of serverless architecture**. Serverless is the big picture (no server management), and FaaS is **one way to achieve it**—by breaking apps into small, independent functions that run on demand.

### **AWS Lambda = FaaS in Action**
AWS Lambda is one of the best-known FaaS platforms. You write a function, upload it, and AWS runs it when triggered—whether it's an API request, a file upload, or a database change. No need to set up a server, manage scaling, or pay when it’s idle.

### **Why Use FaaS?**

- **No Infrastructure Worries** – Just write functions and deploy.
- **Scales Automatically** – One user or a million? No problem.
- **Cost-Effective** – Pay **only** for the execution time.
- **Event-Driven** – Functions run only when something triggers them.


