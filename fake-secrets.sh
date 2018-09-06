#!/bin/bash
cat secrets.yaml | sed 's/[ ].*//' > fake_secrets.yaml
