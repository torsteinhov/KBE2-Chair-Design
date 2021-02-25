# KBE2-Chair-Design
This project challenged us with creating an automated system for chair-manufacturing. We based this on KBE which enables us to capture and systematically reuse product and process
engineering knowledge, with the final goal of reducing time and costs of product development. By this we strive to accomplish automation of repetitive and noncreative design tasks.

We made an interface accessible from the web, where customers was able to input wanted dimensions and production engineers could input production limitations. Based on the input, the data is sent to a template DFA file and updated to be displayed in Siemens NX. The project had the goal of automating a process by enabling multiple systems and making them interract with eachother.

<h2>Product render</h2>
<p align="center">
<img src="https://user-images.githubusercontent.com/77832956/107939730-6d4d9080-6f87-11eb-8647-1d85c32ee681.png">
</p>

   Example with circle shape  |  Example with cross shape
:----------------------------:|:----------------------------:
![](https://user-images.githubusercontent.com/77832956/109148115-19e8f880-7766-11eb-8281-2f0703df2a68.png)  |  ![](https://user-images.githubusercontent.com/77832956/109148159-2705e780-7766-11eb-8c0c-71c2c576eb49.png)

<h2>Architecture</h2>
<p align="center">
<img src="https://user-images.githubusercontent.com/77832956/109137207-3b8fb300-7759-11eb-8047-7cb75d5b3a0a.png">
</p>

<h3>DFAServer.py</h3>

**Main processing unit behind this application. Uses HTTP Requests to retrieve data from the userinterface.html and uploads it to Fuseki database which is based
on the chair_data.kbe ontology through the uploadData method. Retrieves data from feasibilityChecker, and based on the result, overwrites one of the DFA template files to produce the final product for the customer.**

| Method | Functionality |
| --- | --- |
| do_HEAD | sends the headers it would send for the equivalent GET request. |
| do_GET | Gets a request from the path given |
| do_POST | Posts a request to the path given |
| uploadData | Method that deletes data thats already in the database and then defines query for uploading user data to Fuseki, and posts it. |

<h3>manufChecker.py</h3>

**Similar to DFAServer but with handling of the manufacturing constrains from manufCheckerInterface.html. Uploads to Fuseki database which is based on the chair_kbe.kbe
ontology through the setConstrain method.**

| Method | Functionality |
| --- | --- |
| do_HEAD | sends the headers it would send for the equivalent GET request. |
| do_GET | Gets a request from the path given |
| do_POST | Posts a request to the path given |
| setConstrain | Method that deletes data thats already in the database and then defines query for uploading manufacturing constrains to Fuseki, and then posts it. |

<h3>feasibilityChecker.py</h3>

**Retrieves user data and manufacturing constrains from two separate Fuseki servers and checks that the given customer input is within the constrain interval set by the
manufacturer. Sends an approved or not approved signal to DFAServer regarding manufacturing.**

| Method | Functionality |
| --- | --- |
| materialCalculation | Not developed for this project, but added for scalability and further development. |
| retrieveManufaqConstrains | Sends get request to Fuseki, chair_kbe ontology, to retrieve manufacturing constrains from database. |
| retrieveCustomerData | Sends get request to Fuseki, chair_data ontology, to retrieve customer data from database. |
| feasibilityCheck | Brain behind this script, checks the customer data up against the manufacturing constrains intervals, return a boolean value. |
