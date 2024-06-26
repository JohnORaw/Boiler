# Boiler
Digital twin of a domestic boiler.

One of the biggest sinks of energy in my house is my boiler. The original design (1996!) was to have many heat sources, so we would always have hot water. 

- There is an old style Stanley Donard Range which gravity heats the boiler. At 65C a pump kicks in to circulate water through the radiators. This burns mostly wood and is also used for non-polluting waste disposal (no plastic!).
- There is a Riello oil burner. This kicks in on a timer at night and may be used manually in the coldest times of year.
- There is an immersion, used for 15 minutes in the moring before showers, when there is no hot water.
- There are 14 radiators downstairs and 8 upstairs. They have zone switches so I can isolate up and down. I have Shelly switches to automate this later in the project. Each radiator has a thermostatic valve.

One little bit at a time, this project will model the heating system.
The first iteration (2021) uses six temperature sensors to give a view of the instantaneous state of the boiler.
There is also ambient temperaure, pressure and humidity measurement (2022).
After this, it is going to be a matter of adding one bit of thermodynamics at a time (>=2024).
The goal; make the model match reality to a known accuracy with known limits.

The definition of a digital twin, now there's a contentious issue. Does this need to be Laplace's daemon before its a digital twin? Nope, I'm chasing useful functionality, not a defeat of chaos theory.
I'm going to go with a goal of a model which reflects a real system, which can be fed with archival/real/simulated data to provide useful analysis. I need to understand the domain within which the model is valid and the magnitude of the error bars.

Before anyone points out the lack of enviromental friendlyness, I live in Donegal, where regulatory and political incompetence has left many people with soluble houses (!).
The two government schemes to address this are an exercise in cynical politics, most of us consider these schemes to be an unusable excuse to say they have done something.
And don't talk about green policies, the last scheme (which had the green party in government) requires people to rebuild to 2008 standards, reuse old windows, etc.
So I'm as environmentally friendly as I can afford to be, despite government policy.

1. The 1-wire temperature sensors demo code and hardware can be reviewed 
[here.](https://github.com/JohnORaw/DS18B20)

2. The BME280 with ambient temperature, pressure and humidity can be reviewed
[here.](https://github.com/JohnORaw/BME280)

3. Next addition is for three ultrasonic flow transducers.
