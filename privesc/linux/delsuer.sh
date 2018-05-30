#!/bin/bash

echo "[*] Delete user: offsec"

userdel --force offsec
sed '/offsec/d;//d' -i /etc/passwd
sed '/offsec/d;//d' -i /etc/shadow
sed '/offsec/d;//d' -i /etc/sudoers

echo "[*] OK"
