# Pi-Temperature

**Pi-Temperature** is a project designed to monitor and manage the temperature in a server room using a Raspberry Pi and a DHT22 temperature sensor. The system ensures that if the air conditioning in the server room fails and the temperature exceeds a certain threshold, a relay is triggered to take corrective action, and all data is sent to the Zabbix monitoring system for alerting and notifications.

## Features

- **Temperature Monitoring**: Uses a DHT22 sensor to continuously monitor the room temperature.
- **Automated Relay Trigger**: When the temperature exceeds a set threshold, a relay is triggered to take action (e.g., hard reseting on a cooling system).
- **Zabbix Integration**: All temperature data is sent to a Zabbix monitoring system, which can trigger email notifications based on temperature changes.
- **Email Notifications**: The Zabbix system sends email alerts when the server room temperature exceeds critical levels, ensuring timely responses.

## Prerequisites

Before using this system, ensure the following:

- Raspberry Pi with a running Linux-based OS (e.g., Raspbian).
- DHT22 temperature sensor connected to the Raspberry Pi.
- Solid-State Relay (SSR): A relay module designed without physical contacts, using electronic components (such as transistors and optocouplers) to switch the circuit, providing faster and more reliable switching
- Zabbix monitoring system configured to receive temperature data.
- Python 3 and necessary libraries installed.
