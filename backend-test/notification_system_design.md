# Notification System Design

## Overview
The notification system is responsible for alerting users when a vehicle service is due. It works alongside the vehicle maintenance module and uses a logging middleware to track system activity.

---

## Components

### 1. Vehicle Maintenance Module
- Stores vehicle data
- Tracks service schedules
- Identifies due services

### 2. Notification Service
- Generates notifications when a service is due
- Stores notification messages in memory
- Provides APIs to send and retrieve notifications

### 3. Logging Middleware
- Logs important events such as:
  - Notification sent
  - Errors
  - API calls
- Sends logs to external logging API

---

## System Flow

1. A vehicle is added using `/vehicles`
2. Service is scheduled using `/schedule`
3. System calculates next service date
4. `/due-services` identifies vehicles due for service
5. Notification is triggered using `/notify`
6. Notification is stored and can be fetched using `/notifications`

---

## API Endpoints

### Vehicle Module
- POST /vehicles → Add vehicle
- GET /vehicles → Get all vehicles
- POST /schedule → Schedule service
- GET /due-services → Get due vehicles

### Notification Module
- POST /notify → Send notification
- GET /notifications → Retrieve notifications

---

## Data Handling
- Data is currently stored in in-memory lists
- No persistent database is used

---

