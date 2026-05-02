# Notification System Design

## Overview
This system sends notifications to users when important events occur, such as vehicle service due alerts.

## Components
- Vehicle Service Module
- Notification Service
- Logging Middleware

## Flow
1. Vehicle service is scheduled
2. System checks for due services
3. Notification is triggered
4. Notification is stored and sent

## API Endpoints
- POST /notify → send notification
- GET /notifications → retrieve notifications

## Future Improvements
- Add message queue (Kafka/RabbitMQ)
- Add email/SMS notifications
- Retry failed notifications
- Store data in database instead of memory