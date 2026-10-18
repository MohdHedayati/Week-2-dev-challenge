# Local Log Whisperer 🕵️‍♂️🪵

An AI-powered local log diagnostic tool built for the **Hacktoberfest 2026 Week 2 DEV Challenge** (Side Hustle theme). 

## The Problem
Freelance sysadmins and boutique dev shops handle highly sensitive client server logs. They cannot paste these logs into closed-source web UI LLMs without violating NDAs or strict data privacy laws. 

## The Solution
**Local Log Whisperer** is a lightweight diagnostic Python script that ingests local server logs, identifies critical anomalies (like Out-Of-Memory kills and database connection drops), and generates structured, actionable fixes. 

## Features
* **Privacy First:** Designed to target open-weight models (like Gemma 2) to ensure proprietary client data never leaks to unauthorized third parties.
* **Fast Diagnostics:** Automatically categorizes error severity (Low/Medium/High/Critical).
* **Actionable Output:** Provides step-by-step resolution workflows for common server failures.
