#!/bin/bash

DATE=$( date +%F_%T_ )

cp $1 "$DATE$USER.txt"
