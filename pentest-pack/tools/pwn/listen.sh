#!/bin/bash
# simple socat wrapper
socat TCP-LISTEN:$2,reuseaddr,fork EXEC:./$1
