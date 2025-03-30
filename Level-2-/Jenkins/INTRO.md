### **Introduction to DevOps: Why It’s Needed**

To understand DevOps, let’s first look at how a company operates **without DevOps**, following the **Waterfall Model**, which was traditionally used in software development.
### **Software Development Without DevOps (Waterfall Model)**
In a company using the **Waterfall Model**, software development follows a **linear, sequential** process where each phase must be completed before moving to the next.
#### **1️⃣ Requirements Phase:**
- The business team gathers all project requirements upfront.
- Developers, testers, and operations teams do **not** get involved in this phase.

#### **2️⃣ Development Phase:**
- Developers start coding the project **after requirements are finalized**.
- They work for **months** without testing or deployment, leading to late-stage errors.

#### **3️⃣ Testing Phase:**
- After coding is done, testers check for bugs.
- If a major bug is found, developers have to **rework large parts of the code**, delaying the project.

#### **4️⃣ Deployment Phase:**
- The operations team manually sets up servers and deploys the application.
- If issues arise in production, debugging is slow because **developers and operations work separately**.

#### **5️⃣ Maintenance Phase:**
- Fixing issues takes time since developers are already working on new projects.
- Deployments happen **infrequently** (sometimes once every few months).

### **Problems with the Waterfall Model:**
- **Slow Development:** Since testing happens after coding, bugs are caught late, causing major delays.
- **Siloed Teams:** Developers, testers, and operations teams work separately, leading to miscommunication.
- **Manual Deployments:** Setting up servers and releasing software takes a lot of time and effort.
- **Difficult to Adapt:** Changing requirements midway is hard since all planning happens upfront.

Because of these issues, companies started looking for **faster, more collaborative** ways to build and deploy software—this led to the rise of **Agile Development** and later, **DevOps**.

This cascading delivery model is very slow. For any new feature, waterfall model has to be used which makes it very slow. Clients cant get their feedback fast.

---

### **Agile Model: The Evolution from Waterfall**

To address the slow, rigid nature of the **Waterfall Model**, companies adopted the **Agile Model**, which focuses on flexibility, collaboration, and faster releases. Instead of developing the entire product in one go, Agile breaks it into **small, iterative cycles** called **Sprints** (usually 1-4 weeks long).

### **How Agile Development Works**

#### **1️⃣ Requirement Gathering & Planning (Sprint Planning)**

- Instead of collecting all requirements upfront, Agile gathers **high-level requirements** and refines them over time.
- Work is divided into **user stories** (small, independent tasks) and prioritized in a **backlog**.
- A **Sprint** (short development cycle) is planned, typically lasting 1-4 weeks.
    
#### **2️⃣ Development & Continuous Feedback**
- Developers start coding the selected user stories.
- Code is frequently reviewed, and testers work **alongside developers** to catch bugs early.
    
#### **3️⃣ Testing During Development**

- Unlike Waterfall, where testing happens at the end, Agile includes **continuous testing** after each small feature is built.
- If issues arise, they are **fixed immediately**, reducing costly late-stage rework.
    

#### **4️⃣ Frequent Releases & Deployment**
- At the end of every Sprint, a **working version of the software is released** (instead of waiting months for a big release).
- New changes are quickly delivered to users.

#### **5️⃣ Continuous Improvement (Retrospective & Next Sprint)**
- After each Sprint, the team holds a **retrospective** to discuss what worked and what didn’t.
- Feedback is used to improve the next Sprint.

### **Advantages of Agile Over Waterfall**
- Client req are better understood cuz of constant feedback.
✅ **Faster Development:** Features are built and released **incrementally**, rather than waiting months for a full product.  
✅ **Better Collaboration:** Developers, testers, and business teams work **together** rather than in silos.  
✅ **Early Bug Detection:** Continuous testing ensures bugs are caught **early**, reducing rework.    
✅ **Frequent Releases:** Users get updates **every few weeks**, not just once or twice a year.

---
### **Challenges of Agile & The Need for DevOps**

Even with Agile, there are still some problems:

- Code is developed **quickly**, but **deploying and maintaining** software is still slow if done manually.
- Developers write code fast, but if **operations teams take too long to set up infrastructure**, releases are delayed.
- Scaling becomes harder as projects grow.

----

### **DevOps: Bridging the Gap Between Development & Operations**

Even though Agile improved development speed, it didn’t solve the challenges of **deployment, infrastructure management, and operations**. Developers built software **quickly**, but deploying and maintaining it **still took time** due to manual setups. This is where **DevOps** comes in.

### **What is DevOps?**
DevOps (Development + Operations) is a **culture and practice** that focuses on **automation, collaboration, and continuous delivery** to ensure software moves **quickly from development to production**.

### **How DevOps Solves Agile’s Challenges**

#### **1️⃣ Continuous Integration (CI) - Automating Code Integration**

In Agile, developers frequently update code. Instead of manually merging and testing changes, **Continuous Integration (CI)** automates this process.

- Developers push code to a shared repository (e.g., GitHub, GitLab).
    
- **CI tools (like Jenkins, GitHub Actions, CircleCI)** automatically test the code to detect errors early.

#### **2️⃣ Continuous Delivery (CD) - Automating Deployment**

Once code is tested, **Continuous Delivery (CD)** ensures it is automatically deployed to staging or production environments.

- Tools like **Jenkins, GitLab CI/CD, and AWS CodePipeline** automate software releases.
- Frequent, **small releases** reduce the risk of deployment failures.
    
#### **3️⃣ Infrastructure as Code (IaC) - Automating Infrastructure**

Traditionally, setting up servers, databases, and networks was **manual and time-consuming**. With **Infrastructure as Code (IaC)** tools like **Terraform, AWS CloudFormation, and Ansible**, infrastructure can be **automated, versioned, and managed like code**.

- Example: Instead of manually setting up AWS EC2 instances, Terraform can create and configure them automatically.

#### **4️⃣ Monitoring & Logging - Ensuring System Health**

Once deployed, applications need monitoring to ensure they run smoothly. Tools like **Prometheus, Grafana, ELK Stack, and Datadog** help track performance, detect failures, and send alerts.

- Example: If a web app crashes, monitoring tools alert the team so issues can be fixed immediately.

#### **5️⃣ Collaboration Between Dev & Ops**
- DevOps removes the **wall** between development and operations.
- Developers, testers, and sysadmins **work together** to ensure **fast, stable deployments**.
- With tools like **Docker and Kubernetes**, developers can run the same environment locally and in production, reducing deployment issues.
    
---

### **DevOps in Action: A Typical Workflow**

#### **1️⃣ Code Push & Continuous Integration**
- Developers push code to GitHub.
- Jenkins automatically triggers a **CI pipeline**, compiles code, and runs unit tests.

#### **2️⃣ Build & Containerization**
- If tests pass, the application is **packaged into a Docker container**.

#### **3️⃣ Deployment to a Staging Environment**
- Jenkins/CD tools deploy the container to a **staging server** for further testing.

#### **4️⃣ Continuous Monitoring**
- Prometheus & Grafana monitor system performance.
- If a server crashes, alerts are sent.
    
#### **5️⃣ Production Deployment & Scaling**
- Kubernetes scales the app based on traffic.
- Canary or Blue-Green Deployments ensure zero-downtime releases.

---

### **Why DevOps? The Key Benefits**

✅ **Faster Releases:** Automating testing & deployment means software reaches users faster.  
✅ **Fewer Bugs in Production:** Continuous testing detects errors early, reducing failures.  
✅ **Scalability & Reliability:** Cloud-based automation ensures smooth scaling.  
✅ **Better Collaboration:** Devs & Ops work together instead of blaming each other.  
✅ **Cost Savings:** Automation reduces manual effort & infrastructure costs.

---

![[Pasted image 20250329130140.png]]

### **DevOps Lifecycle: The Continuous Development & Deployment Cycle**

The DevOps lifecycle is a continuous cycle of **planning, coding, building, integrating, deploying, operating, and monitoring** software. It ensures **faster delivery, automation, and stability** in software development.

---
### **1️⃣ Plan → Defining Requirements & Roadmap**

Before development starts, teams **plan features, set goals, and define architecture**. Agile methodologies like **Scrum and Kanban** are commonly used.

🔹 **Tools:**
- **JIRA, Trello, Asana** – Track tasks, sprints, and progress.
- **Confluence** – Document architecture and workflows.

📌 **Example:** A team uses JIRA to define user stories and assign tasks for a new feature.

---

### **2️⃣ Code → Writing & Managing Source Code**

Developers write code following best practices, keeping it version-controlled and collaborative.

🔹 **Tools:**
- **Git (GitHub, GitLab, Bitbucket)** – Version control to manage and track code changes.
- **VS Code, IntelliJ, PyCharm** – IDEs for efficient development.
- **SonarQube, Snyk** – Code quality and security analysis.
    
📌 **Example:** A developer writes a new feature and pushes the code to GitHub.

---

### **3️⃣ Build → Compiling & Packaging Code**

The source code is **converted into executable software**. Dependencies are managed, and the application is packaged (e.g., as a JAR, WAR, or Docker container).

🔹 **Tools:**
- **Maven, Gradle** – Java-based build automation tools.
- **Docker** – Packages applications into containers for consistent deployment.
- **JFrog Artifactory, Nexus** – Stores built artifacts for deployment.

📌 **Example:** A Java project is built using Maven, and the output JAR is stored in Artifactory.

---

### **4️⃣ Integrate → Continuous Integration (CI) & Automated Testing**

Developers merge code frequently, triggering **automated builds, tests, and security scans**.
🔹 **Tools:**
- **Jenkins, GitHub Actions, GitLab CI/CD** – Automate build & test processes.
- **Selenium, JUnit, TestNG** – Automated testing frameworks.

📌 **Example:** Jenkins detects a new code commit, compiles it, runs tests, and ensures it is stable before merging.

---

### **5️⃣ Deploy → Continuous Deployment (CD) & Release Management**

Once tested, the software is **deployed to staging and production environments** automatically.
🔹 **Tools:**
- **Jenkins, AWS CodeDeploy, Spinnaker** – Automate deployments.
- **Terraform, Ansible** – Automate infrastructure provisioning.
- **Kubernetes, OpenShift** – Deploy and scale containerized applications.
    
📌 **Example:** Jenkins deploys a new microservice to a Kubernetes cluster without downtime.

---

### **6️⃣ Operate → Managing Infrastructure & Application Stability**

Ensuring the system runs **smoothly and efficiently** after deployment.
🔹 **Tools:**
- **Terraform, AWS CloudFormation** – Automate cloud infrastructure.
- **Ansible, Chef, Puppet** – Configuration management for maintaining servers.
- **Kubernetes** – Manages containerized applications at scale.

📌 **Example:** Terraform provisions an AWS EC2 instance, and Ansible installs necessary software.

---
### **7️⃣ Monitor → Tracking Performance & Logging**

The application and infrastructure are continuously monitored for **errors, performance issues, and security threats**.
🔹 **Tools:**
- **Prometheus & Grafana** – Monitor system performance & create dashboards.
- **ELK Stack (Elasticsearch, Logstash, Kibana)** – Collect and analyze logs.
- **New Relic, Datadog, Splunk** – Cloud-based monitoring & alerting.
    
📌 **Example:** If CPU usage spikes on a server, Prometheus alerts the team for quick resolution.

---
### **The Continuous DevOps Cycle**

Once monitoring is done, insights are fed back into the **Plan** stage to improve future releases, ensuring **continuous development, automation, and delivery**.

---

### **Summary: Why This Lifecycle Matters?**

✅ **Fast Releases:** Automated CI/CD ensures quick software delivery.  
✅ **Early Issue Detection:** Continuous Integration helps catch bugs early.  
✅ **Scalability:** Containerization & IaC automate infrastructure growth.  
✅ **Reliability:** Monitoring tools ensure system stability.


---


# CI / CD :
CI/CD stands for **Continuous Integration and Continuous Deployment/Delivery**, a practice in software development aimed at automating the process of building, testing, and deploying code changes. 

- **Continuous Integration (CI)** ensures that whenever developers make changes to the code, these changes are automatically merged into a shared repository, built, and tested to identify issues early.

- **Continuous Deployment (CD)** automates the release process, pushing changes to production automatically after passing all tests, while **Continuous Delivery** prepares the code for deployment but requires manual approval to push it live. 

![[Pasted image 20250329122611.png]]

### **CI/CD Explained with a Food Delivery App Example** 🚀

CI/CD (Continuous Integration & Continuous Deployment/Delivery) automates software development, testing, and deployment to ensure **fast, stable, and reliable releases**.

#### **Without CI/CD (The Old Way)**

Developers work on different features like **"faster search"** and **"discount offers"** separately. When they try to merge, conflicts arise, leading to broken code, delayed releases, and manual deployment.

#### **With CI/CD (The Automated Way)**

Developers push small code changes frequently, and tools like **Jenkins** automatically test, merge, and deploy updates.

- **CI (Continuous Integration):** Every small code update is automatically built and tested when pushed to a shared repository (like GitHub). If tests fail, developers are notified immediately. This ensures code is always **stable** and ready to deploy.
    
- **CD (Continuous Delivery):** The tested code is deployed to a **staging environment**, where it can be manually approved for release. The app is always ready to go live without delays.
    
- **CD (Continuous Deployment):** The latest working version is **automatically deployed** to production without manual approval, meaning users instantly get new features or bug fixes.
    

#### **How Jenkins Fits In**
Jenkins automates the CI/CD pipeline by fetching code, building the application, running tests, and deploying updates. A typical Jenkins pipeline:

1. **Developer Pushes Code** → GitHub
2. **Jenkins Triggers Pipeline** → Builds, Tests, and Deploys Automatically
3. **If Tests Pass** → The app is deployed to **staging/production**
    
This setup ensures **fast releases**, **fewer bugs**, and **happier users**

---

# **Jenkins: An Automation Platform for CI/CD**

Jenkins is an **automation platform** that allows you to **build, test, and deploy** software using pipelines. It is widely used in **Continuous Integration (CI) and Continuous Deployment (CD)** to streamline the software development process.

### **How Jenkins Works in CI/CD**
Jenkins automates the process of integrating code changes, testing them, and deploying applications efficiently. A typical Jenkins pipeline follows these steps:

1. **Code Commit:** Developers push code to a version control system like GitHub or GitLab.
2. **Build Process:** Jenkins automatically pulls the latest code, compiles it, and prepares it for testing.
3. **Automated Testing:** The pipeline runs unit, integration, and other tests to ensure the new code doesn’t break anything.
4. **Deployment:** If all tests pass, the software is deployed to a staging or production environment.
    
### **Other Uses of Jenkins for Automation**

Besides CI/CD, Jenkins can automate many tasks in software development and IT operations, such as:

- **Infrastructure as Code (IaC):** Automating server provisioning using tools like Terraform and Ansible.
- **Cloud Deployments:** Deploying applications to AWS, Azure, or Kubernetes clusters.
- **Security Scanning:** Running automated security checks on code and dependencies.
- **Database Migrations:** Automating schema changes and data updates.
- **Performance Testing:** Running load tests to ensure application scalability.
- **Backup and Monitoring:** Scheduling automated backups and integrating with monitoring tools like Prometheus.

### **Why Use Jenkins?**

✅ Open-source and highly extensible with plugins.  
✅ Supports integration with Git, Docker, Kubernetes, and cloud platforms.  
✅ Provides both **declarative** and **scripted** pipelines for flexibility.  
✅ Automates repetitive tasks, reducing manual effort and human errors.

--- 

### **Jenkins Infrastructure: Master-Server and Agents**

Jenkins follows a **Master-Agent** architecture, which helps in distributing workloads efficiently.
### **1️⃣ Jenkins Master-Server**

- The **Master Server** is the central control unit that manages Jenkins pipelines, schedules jobs, and coordinates agents.
- It handles UI interactions, job configurations, and monitoring.
- It does **not** perform heavy build tasks to prevent overloading.

### **2️⃣ Jenkins Agents (Nodes/Slaves)**

- Agents are **worker machines** that execute build, test, and deployment tasks.
- They run on separate machines to handle specific workloads (e.g., compiling code, running tests, deploying software).
- Multiple agents can work in parallel to speed up the process.
    

---
### **Example Jenkins Workflow with Master-Agent Setup**

#### **Step 1: Developer Pushes Code**
A developer commits code to GitHub/GitLab.
#### **Step 2: Jenkins Master Becomes Aware**
- The **Jenkins Master** detects the code change (via Webhook or Polling).
- It **schedules a build** and assigns it to an available agent.
#### **Step 3: Agent Pulls and Builds Code**

- The assigned **Jenkins Agent** pulls the latest code.
- It **compiles** the application (if necessary) and runs necessary **unit tests**.
    
#### **Step 4: Automated Testing on Multiple Agents**

- If needed, different **agents run tests in parallel** (e.g., frontend, backend, security scans).
- If a test fails, Jenkins notifies the developer.
    
#### **Step 5: Deployment to Staging/Production**

- If all tests pass, the **agent deploys the application** to a staging or production server.
- Cloud-based agents can be used for deploying to **AWS, Azure, Kubernetes**, etc.
    
#### **Step 6: Monitoring and Cleanup**

- Jenkins monitors the application health after deployment.
- Logs and artifacts are stored for debugging.
- Unused agents are **freed up for new tasks**.
    
---
### **Why Use Master-Agent Architecture?**

✅ **Scalability:** Multiple agents handle different tasks, preventing bottlenecks.  
✅ **Load Distribution:** The master delegates workloads, keeping the system efficient.  
✅ **Parallel Execution:** Tasks run on different nodes, speeding up builds.  
✅ **Cross-Platform Support:** Agents can run on Linux, Windows, or MacOS.

---

### **Jenkins Agent Types: Permanent & Cloud Agents**

Jenkins agents execute jobs assigned by the master server. They can be **permanent** (always available) or **cloud-based** (dynamically created when needed).
#### **1️⃣ Permanent Agents (Static Nodes)**

Permanent agents run on dedicated machines and remain connected to Jenkins. They are manually configured with a fixed setup and are used for stable workloads like compiling applications or running legacy systems. Since they are always running, they require manual maintenance and updates, making them suitable for predictable, long-term workloads but less scalable.

#### **2️⃣ Cloud-Based Agents (Ephemeral Nodes)**

Cloud agents are created on demand and terminated after job completion, optimizing costs and scalability.

- **Docker Agents**: Jenkins spins up a temporary container for execution, ensuring an isolated and clean environment for every job. This is ideal for testing and microservices.
    
- **Kubernetes Agents**: Jenkins dynamically provisions pods in a Kubernetes cluster, enabling large-scale builds and multi-language CI/CD pipelines with auto-scaling.
    
- **Cloud VM Agents (AWS EC2, Azure, GCP)**: Cloud instances are started when needed and shut down after use, making them suitable for resource-intensive tasks like machine learning or complex builds.
    

Permanent agents are best for consistent workloads, while cloud agents are preferred for dynamic, scalable environments where resources need to be optimized.