# Brake test analysis


## Abstract

This technote describes the analysis on the brake test. The brake test intentionally stops the TMA during the slew to check the safety of how immediately TMA reacts to the brake and measuring the stopping distance by the distance moved between full stop from the point the brake was triggered. We used two ways to give a brake to the telescope, one is using the E-stop, this was done when the M1M3 surrogate mirror was installed on the telescope, and the other one is to use the GIS door interlock, and this was done during the ComCam onsky campaign.  

## Dates and time of the brake test
### Using E-stop 
On 2023.11.23, TMA was tested with 70% speed. (Az: 7 deg/s, El: 3.5 deg/s)
1. Az: 2023-11-23T00:40:35 
2. El: 2023-11-23T01:37:20
---
BLOCK-142 : https://jira.lsstcorp.org/browse/BLOCK-142

### Using GIS door interlock
1. 1% speed set (0.1 deg/s)
    * Az: 2024-11-06 09:20
    * El: 2024-11-06 09:32
2. 2% speed set (0.2 deg/s)
    * Az: 2024-11-08T04:41:43.430Z
    * El: 2024-11-08T05:28:23Z
3. 5% speed set (0.5 deg/s)
    * Az: 2024-11-09 09:44 to 09:46 
    * El: 2024-11-09 10:20 to 10:21
4. 10% speed set (1 deg/s)
    * Az: 2024-11-21 10:40 - 10:42
    * El: 2024-11-21 11:06 - 11:07
5. 20% speed set (2 deg/s)
    * Az: 2024-11-29 20:04
    * El: 2024-11-29 20:08
6. 40% speed set (4 deg/s)
    * Az: 2024-12-08 09:06:11
    * El: 2024-12-08 09:02:22

---
 * Az brake test : BLOCK-T231
 * El brake test : BLOCK-T240

## Cases
### 1-1: Az brake test on 2023-11-23
* time_start = "2023-11-23T00:40:35"
* time_ends = "2023-11-23T00:40:40"
* Event happened at: 2023-11-23T00:40:36.120481

:::{figure} ./_static/1-1.png
:name: Az brake test on 2023-11-23
:target: ../_static/1-1.png
:::

* Stopping distance = 12.87 deg

### 1-2: El brake test on 2023-11-23
* time_start = "2023-11-23T01:37:20"
* time_ends = "2023-11-23T01:37:40"
* Event happened at: 2023-11-23T01:37:23.124712

:::{figure} ./_static/1-2.png
:name: El brake test on 2023-11-23
:target: ../_static/1-2.png
:::

* Stopping distance = 4.46 deg

### 2-1. ComCam onsky: 1% speed Az Brake Test
* time_start = "2024-11-06T09:21:30"
* time_ends = "2024-11-06T09:21:35"
* Event happened at: 2024-11-06T09:21:30.071630

:::{figure} ./_static/2-1.png
:name: Az brake test 1% speed
:target: ../_static/2-1.png
:::

* Stopping distance = 0.091 deg

### 2-2. ComCam onsky: 1% speed El Brake Test
* time_start = "2024-11-06T09:34:43"
* time_ends = "2024-11-06T09:34:50"
* Event happened at: 2024-11-06T09:34:45.864699

:::{figure} ./_static/2-2.png
:name: El brake test 1% speed
:target: ../_static/2-2.png
:::

* Stopping distance = 0.12 deg

### 2-3. ComCam onsky: 2% speed Az Brake Test
* time_start = "2024-11-08T04:42:00"
* time_ends = "2024-11-08T04:42:10"
* Event happened at: 2024-11-08T04:42:05.501016

:::{figure} ./_static/2-3.png
:name: Az brake test 2% speed
:target: ../_static/2-3.png
:::

* Stopping distance = 0.049 deg

### 2-4. ComCam onsky: 2% speed El Brake Test
* time_start = "2024-11-08T05:27:31"
* time_ends = "2024-11-08T05:27:50"
* Event happened at: 2024-11-08T05:27:37.546319

:::{figure} ./_static/2-4.png
:name: El brake test 2% speed
:target: ../_static/2-4.png
:::

* Stopping distance = 0.073 deg

###  2-5. ComCam onsky: 5% speed Az Brake Test
* time_start = "2024-11-09T09:45:11"
* time_ends = "2024-11-09T09:45:16"
* Event happened at: 2024-11-09T09:45:12.544466

:::{figure} ./_static/2-5.png
:name: Az brake test 5% speed
:target: ../_static/2-5.png
:::

* Stopping distance = 0.11 deg

### ComCam onsky: 5% speed El Brake Test
* time_start = "2024-11-09T10:20:45"
* time_ends = "2024-11-09T10:21:10"
* Event happened at: 2024-11-09T10:20:49.569646

:::{figure} ./_static/2-6.png
:name: El brake test 5% speed
:target: ../_static/2-6.png
:::

* Stopping distance = 0.22 deg

### 2-7. ComCam onsky: 10% speed Az Brake Test
* time_start = "2024-11-21T10:41:27"
* time_ends = "2024-11-21T10:41:32"
* Event happened at: 2024-11-21T10:41:28.040349

:::{figure} ./_static/2-7.png
:name: Az brake test 10% speed
:target: ../_static/2-7.png
:::

* Stopping distance = 0.51 deg

### 2-8. ComCam onsky: 10% speed El Brake Test
* time_start = "2024-11-21T11:06:27"
* time_ends = "2024-11-21T11:06:33"
* Event happened at: 2024-11-21T11:06:28.477046

:::{figure} ./_static/2-8.png
:name: El brake test 10% speed
:target: ../_static/2-8.png
:::

* Stopping distance = 0.60 deg

### 2-9. ComCam onsky: 20% speed Az Brake Test
* time_start = "2024-11-29T20:04:25"
* time_ends = "2024-11-29T20:04:32"
* Event happened at: 2024-11-29T20:04:26.418824

:::{figure} ./_static/2-9.png
:name: Az brake test 20% speed
:target: ../_static/2-9.png
:::

* Stopping distance = 1.6 deg

### 2-10. ComCam onsky: 20% speed El Brake Test
* time_start = "2024-11-29T20:09:09"
* time_ends = "2024-11-29T20:09:16"
* Event happened at: 2024-11-29T20:09:09.582050

:::{figure} ./_static/2-10.png
:name: El brake test 20% speed
:target: ../_static/2-10.png
:::

* Stopping distance = 1.91 deg

### 2-11. ComCam onsky: 40% speed Az Brake Test
* time_start = "2024-12-08T09:06:11"
* time_ends = "2024-12-08T09:06:17"
* Event happened at: 2024-12-08T09:06:11.372613

:::{figure} ./_static/2-11.png
:name: Az brake test 40% speed
:target: ../_static/2-11.png
:::

* Stopping distance = 4.88 deg

### 2-12. ComCam onsky: 40% speed El Brake Test
* time_start = "2024-11-29T20:09:09"
* time_ends = "2024-11-29T20:09:15"
* Event happened at: 2024-12-08T09:02:22.303270

:::{figure} ./_static/2-12.png
:name: El brake test 40% speed
:target: ../_static/2-12.png
:::

* Stopping distance = 5.95 deg

### Stopping distance vs speed set
#### Azimuth
:::{figure} ./_static/az_speed_sd.png
:name: Az stopping distance vs speed set
:target: ../_static/az_speed_sd.png
:::

#### Elevation
:::{figure} ./_static/el_speed_sd.png
:name: El stopping distance vs speed set
:target: ../_static/el_speed_sd.png
:::
