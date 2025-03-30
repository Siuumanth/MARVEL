open localhost 8080

# Before Jenkins:

1️⃣ **Inconsistent Code Commits**
- Developers work from different time zones and contribute varying amounts of code.
- No uniform commit schedule leads to irregular code integration.

2️⃣ **Delayed Testing & Integration**
- Developers had to wait until the **entire software** was built and tested to identify errors.
- Bugs were found late in the cycle, making debugging and fixes **time-consuming**.

3️⃣ **No Iterative Improvement**
- Since testing happened at the end, there was **no room for gradual updates**.
- If an issue was found, developers had to **rewrite large sections** of code.

4️⃣ **Slow Software Delivery**
- The entire process took longer because **testing and deployment were manual**.
- A single failure could delay the release by **weeks or even months**.

5️⃣ **Prone to Human Errors**
- Manual processes for **building, testing, and deployment** led to frequent mistakes.
- Deployment failures were common due to lack of **automation**.

---

Jenkins is a CI tool that allows Continuous development, test and deployment of newly created codes.

![[Pasted image 20250329143940.png]]


## Jenkins Pipeline:

1. Code Commit happens to Jenkins
2. Jenkins will create a build of our code, which runs unit tests to validate our code. 
3. After testing, we can release a ready environment in Jenkins.
4. We can Deploy our code to production environment, all these processes are automated.

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

### **Jenkins Terminologies Explained**

#### 1️⃣ **Job (Project) & Build**  
A **job** in Jenkins is a **repeatable task** that automates processes like **building, testing, and deploying software**. Each time a job runs, it creates a **build**, which is an execution instance of that job.
#### 🔹 **How Jobs & Builds Work Together**
- **Jobs act as blueprints**, while **builds are executions of those jobs**.
- Every build is **numbered sequentially** (e.g., Build #10, Build #11) and linked to the job that triggered it.
- Builds store **logs, console output, test results, artifacts (output files), and execution timestamps**.
- If a build **fails**, Jenkins can automatically:
    - **Retry the build** based on retry rules.
    - **Send alerts** (email, Slack, Teams, etc.).
    - **Trigger rollback actions** if necessary.
        
#### 🔹 **Types of Jobs in Jenkins**
1️⃣ **Freestyle Job** – The most basic job type; can be configured using a UI with build steps and triggers.  
2️⃣ **Pipeline Job** – Uses a **Jenkinsfile** to define multi-step CI/CD pipelines as code.  
3️⃣ **Multibranch Pipeline** – Automatically detects Git branches and runs separate pipelines for each branch.  
4️⃣ **Parameterized Job** – Accepts **input parameters** (e.g., environment, version) before execution.  
5️⃣ **Folder Job** – Used for organizing multiple jobs into categories.

#### 🔹 **What Happens When a Build Runs?**
1. Jenkins fetches the latest code from the **Git repository**.
2. The code is **compiled or processed**, depending on the project type (e.g., Java builds with Maven, Node.js installs dependencies).
3. Automated **tests are executed** to check for errors or regressions.
4. If successful, Jenkins may **package the build into an artifact** (e.g., `.jar`, `.zip`, Docker image).
5. The final artifact is **deployed to staging or production** if configured.
6. Jenkins provides a **detailed report** of the build, including logs, success/failure status, and test results.

#### 2️⃣ **Pipeline & Jenkinsfile**  
A **pipeline** is an automated CI/CD workflow that contains multiple steps for **code integration, testing, and deployment**. Pipelines are defined using a **Jenkinsfile**, which is a script stored in the **Git repository** along with the code. This allows Jenkins to pull the latest code changes and execute the predefined workflow automatically.

#### 3️⃣ **Stages & Steps**  
A pipeline is divided into **stages**, which group similar tasks together, such as **Build, Test, and Deploy**. Each stage contains **steps**, which define the individual actions Jenkins needs to perform. For example, the **Build stage** might have steps to **compile code and generate artifacts**, while the **Test stage** runs unit tests and reports results.

#### 4️⃣ **Master & Agents (Nodes & Executors)**  
Jenkins follows a **master-agent** architecture where the **master server** coordinates all jobs, while **agents (worker nodes)** execute them. Agents can be **permanent (dedicated machines) or dynamic (Docker, Kubernetes pods, cloud instances)**. Each agent has **executors**, which are threads that allow multiple jobs to run in parallel on the same machine.

#### 5️⃣ **Workspace & Artifact**  
Each Jenkins job runs in a **workspace**, which is a directory where Jenkins downloads the source code, installs dependencies, and executes tasks. After the job runs, it may produce an **artifact**—the final output of the process, such as a compiled `.jar` file, a Docker image, or a deployment package. Artifacts can be stored and used in later pipeline stages, such as deploying to production.

#### 6️⃣ **Triggers & Scheduling**  
Jenkins jobs can be **triggered automatically** based on events. The most common triggers are:
- **SCM Trigger**: Jenkins detects new Git commits and starts a build.
- **Webhook Trigger**: A push event from GitHub/GitLab triggers a job.
- **Cron Scheduling**: Jobs run at fixed intervals (e.g., every night at 2 AM).
- **Dependency Trigger**: A job runs after another job completes.
    

7️⃣ **Test Reports & Notifications**  
Jenkins integrates with testing frameworks to generate **test reports**, which provide insights into code quality. If tests fail, Jenkins can send **notifications** via email, Slack, or other tools to alert the team and prevent faulty code from reaching production.

This covers the key **Jenkins concepts** needed for CI/CD automation! 🚀

---
# Creating job:

new item > build steps > execute windows batch command > "echo "Hello my first jenkins job %date% : %time%""

click build now, and tap on the build in the build history, > console output ... you should see the output.

![[Pasted image 20250329161622.png]]

to run job every minute. After this, job gets triggered every minute.

Then i downloaded the role based authorization plugin.
with this, u can assign roles to different users in a team- you can give each an accessabilty setting.

## Creating a Git Job:
create job > source code management-select Git  next > add git repo URL > add ur credentials 

![[Pasted image 20250329163638.png]]
This will be responsible for running the java file.

Then after all that, press build now, and see if u got the output.

![[Pasted image 20250329163825.png]]

Successfully ran it - sum 8

### Imp:
Whatever tasks u give for the script, the execution , cloning of git repo will be stored in the workspace folder in your PC.

# Jenkins file:
is a Jenkins as a code.

```js
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Siuumanth/jenkins-test.git' 
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'npm install'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'npm test'
            }
        }
        stage('Start App') {
            steps {
                bat 'node server.js'
            }
        }
    }

}
```

This **Jenkinsfile** defines a **Jenkins Pipeline** to automate the CI/CD process for a Node.js application. It consists of multiple **stages**, each executing specific steps. Let’s break it down:

---

### **1️⃣ `pipeline {}` – Defining a Pipeline**

- The entire Jenkins pipeline is enclosed in the `pipeline {}` block.
- It specifies how the job should execute.
    
---
### **2️⃣ `agent any` – Choosing an Agent**
- `agent any` tells Jenkins to run this pipeline on **any available machine (node/agent).**
- If you have multiple Jenkins agents, Jenkins picks one automatically.
    
---
### **3️⃣ `stages {}` – The Pipeline Workflow**
- A pipeline consists of multiple **stages**, which help organize the workflow.
    
---
### **4️⃣ `stage('Checkout')` – Cloning the Repository**


`stage('Checkout') {     steps {         git 'https://github.com/your-repo.git'  // Change this to your repo     } }`

- This stage **fetches the latest code** from the given GitHub repository.
- The `git` command clones the repo so Jenkins can work with the latest files.
    
---
### **5️⃣ `stage('Install Dependencies')` – Installing npm Packages**

`stage('Install Dependencies') {     steps {         bat 'npm install'     } }`

- Runs `npm install` to install project dependencies (like Express, Jest, etc.).
- **`bat`** is used for Windows (use `sh` for Linux/macOS).
- If `package.json` is present, it installs all necessary packages.
---

### **6️⃣ `stage('Run Tests')` – Running Tests**

`stage('Run Tests') {     steps {         bat 'npm test'     } }`

- Runs **automated tests** (if defined in `package.json` under `"scripts": { "test": "jest" }` or Mocha, etc.).

- Jest will run unit tests and check the code factoring.

- Ensures the application is working before deployment.

---

### **7️⃣ `stage('Start App')` – Running the Application**


`stage('Start App') {     steps {         bat 'node server.js'     } }`

- Starts the Node.js app using `node server.js`.
- If the app runs successfully, Jenkins confirms that everything is working.

---
### **Overall Workflow**
1. **Checkout** – Clone repo from GitHub.
2. **Install Dependencies** – Run `npm install`.
3. **Run Tests** – Execute `npm test` to verify the code.
4. **Start App** – Launch the application.



# Running express js APP:


## **Step 1: Setting up the Node.js Project**

 Create `server.js`

```javascript
const express = require("express");
const path = require("path");

const app = express();
const port = 3000;

// Serve static files from the current directory
app.use(express.static(__dirname));

// Handle all requests
app.get("*", (req, res) => {
    const filePath = path.join(__dirname, req.path === "/" ? "index.html" : req.path + ".html");

    if (path.extname(filePath) === ".html") {
        res.sendFile(filePath, (err) => {
            if (err) {
                res.status(404).send("404 : File not FOUND MACHA");
            }
        });
    } else {
        res.status(404).send("Invalid request");
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
```

### 4. Create `package.json`

```json
{
  "name": "dockertest",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "test": "echo \"No tests found, skipping...\" && exit 0",
    "start": "node server.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.21.2"
  }
}
```

---

## **Step 2: Creating the Jenkins Pipeline**

### 1. Create a `Jenkinsfile` in the root of your project

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo.git' 
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'npm install'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'npm test'
            }
        }
        stage('Start App') {
            steps {
                bat 'node server.js'
            }
        }
    }
}
```

---

## **Step 3: Pushing the Code to GitHub**

---

## **Step 4: Setting Up Jenkins**

### 1. Open Jenkins Dashboard (`http://localhost:8080`)

### 2. Create a New Pipeline Job:

- Click **New Item**
- Enter a name (e.g., `NodeAppPipeline`)

### 3. Configure the Pipeline:
- Scroll down to **Pipeline** section
- Select **Pipeline script from SCM**
- Choose **Git** as SCM
- Enter your **GitHub repository URL**
- Leave other settings as default and **Save**

---

## **Step 5: Running the Pipeline**

### 1. Click **Build Now** in Jenkins

### 2. Output Logs

```bash
Started by user
Obtained Jenkinsfile from GitHub
Running on Jenkins in workspace
Installing dependencies...
Running tests...
"No tests found, skipping..."
Starting application...
Server is listening on port 3000
```

### 3. Check if the server is running by visiting `http://localhost:3000`

---

## **Step 6: Next Steps**

- **Automate Deployment:** Integrate with Docker or a cloud provider
- **Run in Background:** Modify Jenkinsfile to keep the server running
- **Add Testing:** Implement actual test cases (e.g., with Jest)
    

This completes the **Jenkins CI/CD setup for a Node.js Express app**! 

```bash
to stop jenkins on 8080, do 
net stop jenkins

for starting do 
net start jenkins

```

