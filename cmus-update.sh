#!/bin/bash
# Source: https://medium.com/@johnnymatthews/how-to-update-your-cmus-library-73b1282f7d51

cmus-remote -C clear
cmus-remote -C "add ~/Music"
cmus-remote -C "update-cache -f"
