# Distributed Key-Value Store with etcd

This project implements a simple distributed key-value store using etcd as the backend storage. It provides a user interface for interacting with the key-value store through a web interface.
## Setup
1. Install Python and Flask.
2. Install etcd and configure a single-node cluster locally.
3. Clone this repository.

## Running the Application
1. Navigate to the project directory.
2. Run `python app.py`.
3. Access the application in your web browser at `http://localhost:5000`.

## Functionality
- **Put**: Allows users to add key-value pairs to the store.
- **Get**: Retrieves the value associated with a given key.
- **Delete**: Deletes a key-value pair from the store.
- **List**: Lists all keys currently stored in the store.

## Error Handling
- Handles connection errors when unable to connect to the etcd server.
- Provides appropriate error messages for key not found errors.

# Team2_CCProject4_GSEC            
Pragnya Vempati - PES2UG21CS380                                                                              
Prajwal V Shenoy - PES2UG21CS383                                                         
Prerana M - PES2UG21CS398                                                             
Sowmya M N -PES2UG22CS820                                                      
