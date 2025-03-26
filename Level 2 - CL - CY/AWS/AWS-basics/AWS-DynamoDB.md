# What is it?

Amazon **DynamoDB** is a **fully managed NoSQL database service** by AWS, designed for **high availability, scalability, and low-latency performance**. It uses a **key-value and document-based storage model**, making it ideal for applications requiring fast and predictable performance at any scale. 

Unlike traditional relational databases, DynamoDB does not require predefined schemas, allowing flexible data structures. It automatically handles **replication, backups, and scaling**, making it a great choice for real-time applications like gaming, IoT, and session management. DynamoDB also supports **on-demand or provisioned capacity modes** and integrates with AWS services like Lambda for serverless applications.

It is ideal for applications with **known access patterns**. It has guaranteed horizontal scalability. It integrates well with other AWS services.

#### Accessing:
They can be accessed through APIs/ORMs and authorized IAM (Identity Access Management).


## Core Concepts - Tables, Items, Attributes, Indexes.

- `Tables` : Collection of items, like a typical table.
- `Items`: are collection of Attributes, or key/value pairs. Attributes are different column names, and the data under them along with the attributes are items.

### **Primary Keys in DynamoDB**

DynamoDB uses a **primary key** to uniquely identify each item in a table. There are two types of primary keys:

1. **Partition Key (Simple Primary Key)**
    - Acts like the **primary key** in a SQL database.
    - Must be **unique for every item** in the table.
    - Determines how data is distributed across partitions in DynamoDB.
    - Example: In an `Orders` table, if `order_id` is the partition key, each order must have a unique `order_id`.
        
2. **Partition Key + Sort Key (Composite Primary Key)**
    - The **Partition Key** can have duplicates, but only when the **Sort Key** values are different.
    - The **Sort Key** ensures that items with the same Partition Key are **stored together** and **sorted** for efficient querying.
    - Example:
        - Consider an `Orders` table where:
            - `customer_id` is the **Partition Key** (customers can have multiple orders).
            - `order_date` is the **Sort Key** (orders are sorted by date for each customer).
        - A customer (`customer_id = 123`) can have multiple orders with different `order_date` values.
        - Querying for `customer_id = 123` will return all their orders, sorted by date.

#### **Why Use a Sort Key?**
- It allows efficient range queries, like **"Get all orders of a customer in the last 30 days"**
- It enables sorting **without extra processing**.  
- It allows multiple records under the same partition key, avoiding data duplication.
 ![umm](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2018/09/10/dynamodb-partition-key-1.gif)


An **access pattern** in DynamoDB refers to how your application reads and writes data—essentially, the queries you will run. Since DynamoDB is designed for fast lookups with predefined queries, you should model your table structure based on these access patterns rather than traditional relational design.

# Creating a dynamoDB:

1. Navigate to the page in AWS, and click on create table.

We will be creating an `Orders` table. Sort ID cannot be added later, so make an important decision here

- Partition key - OrderId
- Sort Key - CreationDate

2. Customize settings
     - Read Write Capacity settings:
     -` On Demand` - Simplify billing by paying for the actual reads and writes your application performs.
     - `Provisioned` - Manage and optimize your costs by allocating read/write capacity in advance.

Put Auto scaling - off

### **Capacity units**
in DynamoDB determine how much read and write throughput your table can handle. There are two types:
3. **Read Capacity Units (RCUs)** – 1 RCU allows:
    - **1 strongly consistent read** per second for items up to 4 KB.
    - **2 eventually consistent reads** per second for items up to 4 KB.
    
4. **Write Capacity Units (WCUs)** – 1 WCU allows:
    - **1 write per second** for items up to 1 KB.

Adjust the capacity units:
- MinCU - 5, MaxCU-1000

### **Secondary Indexes**

It's like the sort key, but it allows you to create **additional ways to query your data** without modifying the primary key structure. Secondary indexes let you efficiently query attributes that are not part of the main partition key.
#### **Types of Secondary Indexes**

1. **Local Secondary Index (LSI)**
    - **Same partition key** as the base table but with a **different sort key**.
    - Useful when you need multiple ways to sort data within the same partition.
    - Can only be created **at table creation time** (not later).
    - Supports **strongly consistent reads**.
    - Example: A "Users" table with `user_id` as the partition key, but LSIs for sorting by `created_at` or `last_login`.
        
2. **Global Secondary Index (GSI)**
    - **Different partition key and sort key** from the base table.
    - Allows querying data using completely different attributes.
    - Can be added **at any time** after table creation.
    - Only **eventually consistent reads** (by default).
    - Example: A "Orders" table with `order_id` as the main partition key, but a GSI on `customer_id` to query all orders by a customer.
        
LSIs are useful for **alternate sorting within partitions**, while GSIs enable **entirely new access patterns**.

#### Encryption:
You can add to encrypt your data while communicating.

### After Creating Table:
You get directed to the tab where you can find **Overview, Indexes, Monitor, Alarms, and more**.
- The **Overview** section provides general details about the table, such as item count, storage size, and read/write capacity settings. 
- The **Indexes** tab shows both **Global Secondary Indexes (GSI)** and **Local Secondary Indexes (LSI)**, allowing you to manage and optimize query performance. 
- The **Monitor** tab provides real-time metrics like read/write throughput, throttling events, and latency, helping track performance. 
- The **Alarms** section lets you set up alerts for specific thresholds, such as high read/write usage or throttling issues. These tabs collectively help manage, monitor, and optimize your DynamoDB table efficiently.
