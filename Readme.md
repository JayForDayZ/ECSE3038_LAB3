    GET /profile - This route retrieves the user profile information. The client sends a GET request to this endpoint and the server returns the profile data as a JSON object.

    POST /profile - This route creates a new user profile. The client sends a POST request with the profile data in JSON format, and the server stores this information in the database.

    POST /data - This route allows clients to post data to the server. The client sends a POST request with the data in JSON format, and the server stores this information in the database.

    GET /data - This route retrieves all the data that has been posted to the server. The client sends a GET request to this endpoint and the server returns a list of all the data as JSON objects.

    PATCH /data/:id - This route updates a specific data item that was previously posted to the server. The client sends a PATCH request to this endpoint with the updated information, and the server updates the corresponding item in the database.

    DELETE /data/:id - This route allows the client to delete a specific data item that was previously posted to the server. The client sends a DELETE request to this endpoint with the id of the item to be deleted, and the server deletes the corresponding item from the database. The server does not return any response to the client once the item has been deleted, but it does send back a suitable response code indicating that an empty response is expected.