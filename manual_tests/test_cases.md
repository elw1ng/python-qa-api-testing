# API Test Cases – GET /posts/1

---

## TC-API-001
Title: Verify status code for valid request

Preconditions:
API server is available

Steps:
1. Send GET request to /posts/1

Expected Result:
Status code is 200

---

## TC-API-002
Title: Verify returned id matches requested id

Preconditions:
API server is available

Steps:
1. Send GET request to /posts/1

Expected Result:
Response field "id" equals 1

---

## TC-API-003
Title: Verify data types of response fields

Preconditions:
API server is available

Steps:
1. Send GET request to /posts/1

Expected Result:
- userId is integer
- id is integer
- title is string
- body is string

---

## TC-API-004
Title: Verify response contains required fields

Preconditions:
API server is available

Steps:
1. Send GET request to /posts/1

Expected Result:
Response contains fields:
- userId
- id
- title
- body


---

## TC-API-005
Title: Verify response for non-existing post

Preconditions:
API server is available

Steps:
1. Send GET request to /posts/999999

Expected Result:
Status code is 404 or empty response object
