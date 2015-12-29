---
layout: post
title: Set up PKI ssh login on OS X
tags:
notebook: Postach.io
---



Some terminology:

Server: The machine you are trying to connect to.
Client: The machine you are trying to connect from.

## Step 1: Create a keypair on the client

```bash
ssh-keygen -t rsa -C "johnj@michaelhaynes.com" -N ""
```

The `-N` option specifies no passphrase, which we need for automatic login.  The `-C` option specifies a comment, which can be used to help identity the key later.

## Step 2: Append the public key to the user@server's authorized_keys file

```bash
cat ~/.ssh/id_rsa.pub | ssh johnj@10.0.10.8 "mkdir -p ~/.ssh; cat >> ~/.ssh/authorized_keys"
```
