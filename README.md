# Summary - Arena Hernandez

- I propose introducing another method for updating orders. Presently, our only option is to utilize the PATCH call with the order ID, which can pose challenges as it limits updates to available orders only. However, what about scenarios where it's essential to modify orders with pending or sold statuses?
  
- I was unable to complete the task of creating a PATCH request in pytest. Despite using a valid order ID, the function I wrote consistently failed. I confirmed the request's functionality using cURL and Postman, both yielding positive results. Given more time, I would have resolved the issue. Meanwhile, I created test cases for the PATCH using Postman, covering all three statuses: pending, sold, and available. This approach allows the test cycle to proceed while I troubleshoot the pytest function. To resolve the issue, I will consult the API documentation, search online, discuss with QA peers, and as a last resort, seek advice from the API developer.
  
- As part of completing the tasks, I fixed the pet's name schema as it was of integer data type instead of string. Additionally, I created a schema for the orders so it can be validated.
  
- I am including the Postman collection I used to test the project in my submission. The collection is located here pytest-api-example/assets/Pytest-API-Example.postman_collection.json.
  
- I have also included screenshots of all the API calls I tested using Postman in the following location of the project: `pytest-api-example/assets/screenshots`.
