#!/bin/bash

# Write to package.json
nano package.json << 'EOL'
{
  "name": "panel-profits-claude",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@tanstack/react-query": "^5.24.1",
    "axios": "^1.6.7",
    "date-fns": "^3.3.1",
    "lightweight-charts": "^4.1.3",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-error-boundary": "^4.0.12",
    "recharts": "^2.12.2",
    "zod": "^3.22
