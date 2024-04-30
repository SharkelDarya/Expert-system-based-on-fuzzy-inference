# Expert-system-based-on-fuzzy-inference
A system using fuzzy logic to assess the weather outside.
<p align="center">
      <img src="https://i.ibb.co/2dW62Qj/wheather.jpg">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/IDE-VS%20Code-2B7FB8" alt="IDE">
</p>

## About
The project implements a system to assess the suitability of weather for various activities based on parameters such as wind speed, temperature, UV index and atmospheric pressure. 
Using fuzzy logic and a set of rules defined for different conditions. The system provides weather suitability assessment for activities at three levels: "low," "medium" and "high".
Equally, it is possible to enter current weather parameters and get an assessment.

## Documentation

### Libraries
**-** **`skfuzzy`**, **`matplotlib`**, **`NumPy`**

### Determination of membership functions for weather factors
- Assign temperature, wind speed, UV index and atmospheric pressure to membership functions (low, medium, high).
  
### Creating fuzzy rules
- Using membership functions, creating fuzzy rules to determine which weather conditions are considered "good," "average" and "bad" for certain activities.
  
### Creating a fuzzy control system
- A fuzzy logic control system is being created that combines fuzzy rules.
  
### Evaluation of suitability
- Using test weather parameters, the fuzzy control system evaluates weather suitability.
  
### Visualization of results
- Displaying membership functions and results of suitability assessments using charts.
  
### User interaction
- Infinite loop, allowing the user to enter weather parameters and get a suitability rating.
  
### Visualization of results
- Displaying some test images and their corresponding real labels.
## Developers

- Darya Sharkel (https://github.com/SharkelDarya)
