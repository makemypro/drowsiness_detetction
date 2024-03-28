# Driver Drowsiness Detection

Driver Drowsiness Detection is a machine learning project aimed at detecting drowsiness in drivers using Convolutional Neural Networks (CNN). This project also incorporates the Google Maps API for calculating the distance and time between two points, as well as functionality for license verification.

## Overview

The Driver Drowsiness Detection project utilizes machine learning techniques to analyze images captured from a driver-facing camera to determine if the driver is exhibiting signs of drowsiness. By analyzing features such as eye closure and head position, the system can issue alerts to the driver to prevent accidents due to drowsiness.

## Features

- Drowsiness detection using CNN
- Integration with Google Maps API for distance and time calculation
- License verification functionality
- Real-time monitoring and alerts

## Requirements

- Python 3.x
- Django
- TensorFlow
- Numpy
- OpenCV
- Google Maps API key

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/driver-drowsiness-detection.git
pip install -r requirements.txt
python manage.py runserver
