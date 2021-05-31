# Api documentation

## Common Headers
- Content-Type: application/json

## POST /vault/new
### Arguments

```json
{
    data:{
        public_key: VAULT PUBLIC KEY                        [string],
        name: VAULT HUMAN READABLE NAME                     [string]
    },

    sign: sign(vault_priv,"{public_key:...,name:...}")      [string]
}
``` 

### Response

```json
{
    status: "success" or ERROR MESSAGE                      [string]
}
``` 

## POST /vault/get
### Arguments

```json
{
    data:{
        public_key: VAULT PUBLIC KEY                        [string],
    },

    sign: sign(vault_priv,"{public_key:...}")               [string]
}
``` 
### Response

```json
{
    data:{
        name: string
        keys: [
            {
                name: KEY NAME,
                value: KEY VALUE
            },
            {
                name: KEY NAME,
                value: KEY VALUE
            }
        ]
    },
    status: "success" or ERROR MESSAGE                      [string]
}
``` 

## POST /pass/add
### Arguments

```json
{
    data:{
        public_key: VAULT PUBLIC KEY                        [string],
        name: PASSWORD NAME                                 [string],
        value: PASSWORD                                     [string]
    },

    sign: sign(vault_priv,"{public_key:...,name: ...}")     [string]
}
``` 
### Response

```json
{
   status: "success" or ERROR MESSAGE                      [string]
}
``` 