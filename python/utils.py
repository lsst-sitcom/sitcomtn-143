#import

import sys, time, os, asyncio, glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl
from datetime import datetime
from astropy.time import Time, TimeDelta

from lsst_efd_client import EfdClient
from lsst.summit.utils.efdUtils import makeEfdClient, getEfdData
from scipy.interpolate import UnivariateSpline

client = EfdClient("usdf_efd")

def plot_az(az, azXs, azVs, event_1=None, event_2=None):
    """
    Args:
        az: azimuth
    
        azXs: 

        azVs: TMA velocity in azimuth direction

    Returns:


    """
    plt.figure(figsize=(16, 15))
    plt.suptitle("lsst.sal.MTMount.azimuth", fontsize=18, fontweight="bold")

    ###########
    # Position
    plt.subplot(4, 1, 1)
    plt.plot(
        az.index,
        az["actualPosition"],
        label="Position",
    )
    plt.plot(
        az.index,
        az["demandPosition"],
        label="demandPosition",
    )
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Position", fontsize=14)
    plt.grid(":", alpha=0.5)  # or alpha=0.3
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12.5, fontweight="bold")
    plt.yticks(fontsize=14)

    # ++++++++++++++++++++++++++++++++++++++++++#
    ############################################
    if event_1 and event_2 is not None:
        # Event line
        event_datetime_1 = event_1.to_datetime()
        event_datetime_2 = event_2.to_datetime()
        event_time1 = pd.Timestamp(event_datetime_1)
        event_time2 = pd.Timestamp(event_datetime_2)
        plt.axvline(
            x=event_time1,
            color="r",
            linestyle="--",
            label=f"status change: {event_time1}",
        )
        plt.axvline(
            x=event_time2,
            color="r",
            linestyle="--",
            label=f"status change: {event_time2}",
        )
        plt.legend()
    ############################################
    # ++++++++++++++++++++++++++++++++++++++++++#

    # Velocity
    plt.subplot(4, 1, 2)
    plt.plot(
        az["actualVelocity"],
        label="Velocity",
    )
    plt.plot(
        az["demandVelocity"],
        label="demandVelocity",
    )

    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Velocity", fontsize=14)
    plt.grid(":", alpha=0.5)  # or alpha=0.3
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12.5, fontweight="bold")
    plt.yticks(fontsize=14)

    # ++++++++++++++++++++++++++++++++++++++++++#
    ############################################
    if event_1 and event_2 is not None:
        # Event line
        event_datetime_1 = event_1.to_datetime()
        event_datetime_2 = event_2.to_datetime()
        event_time1 = pd.Timestamp(event_datetime_1)
        event_time2 = pd.Timestamp(event_datetime_2)
        plt.axvline(
            x=event_time1,
            color="r",
            linestyle="--",
            label=f"status change: {event_time1}",
        )
        plt.axvline(
            x=event_time2,
            color="r",
            linestyle="--",
            label=f"status change: {event_time2}",
        )
        plt.legend()
    ############################################
    # ++++++++++++++++++++++++++++++++++++++++++#

    # Interpolation
    plt.subplot(4, 1, 3)
    plt.plot(
        azXs,
        azVs,
        label="Velocity",
    )
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Velocity", fontsize=14)
    plt.grid(":", alpha=0.5)  # or alpha=0.3
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12.5, fontweight="bold")
    plt.yticks(fontsize=14)

    ###########
    plt.subplot(4, 1, 4)
    plt.plot(
        azXs,
        azAccSpline(azXs),
        label="Interpolated Acceleration ",
    )
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Acceleration", fontsize=14)
    plt.grid(":", alpha=0.5)  # or alpha=0.3
    plt.legend(fontsize=14)
    plt.xticks(fontsize=12.5, fontweight="bold")
    plt.yticks(fontsize=14)

    # disign
    plt.tight_layout()
    plt.show()
    return

def format_time(t_start, t_end):
    """
    formating time
    Arg:
        t_start (str): start time
        t_end (str): end  time
    return:
        start: start time
        end: end time
    """

    start = Time(t_start, scale="utc", format="isot")
    end = Time(t_end, scale="utc", format="isot")
    return (start, end)   

def call_az_data_range(start, end):
    """
    Query the azimuth data in a time period
    
    Arg:
        start (timestamp): test start time   
        end (timestamp) : test end time

    Return: 
        df_az (Dataframe): dataframe for acutal position,
        actual velocity, demand position, demand velcoity, 
        and timestamp

    """
    df_az = getEfdData(
        client,
        "lsst.sal.MTMount.azimuth",
        columns=[
            "actualPosition",
            "actualVelocity",
            "demandPosition",
            "demandVelocity",
            "timestamp",
        ],
        begin=start,
        end=end,
    )
    return df_az 

def call_el_data_range(start, end):
    """
    Same as call_az_data_range except for el.
    
    Arg:
        start (timestamp): test start time   
        end (timestamp) : test end time

    Return: 
        df_el (Dataframe): dataframe for acutal position,
        actual velocity, demand position, demand velcoity, 
        and timestamp for elevation

    """
    df_el = getEfdData(
        client,
        "lsst.sal.MTMount.elevation",
        columns=[
            "actualPosition",
            "actualVelocity",
            "demandPosition",
            "demandVelocity",
            "timestamp",
        ],
        begin=start,
        end=end,
    )
    return df_el

def acc_spline(df_test):
    """
    Spline fitting for     

    """
    elXs = df_test["timestamp"].values - df_test["timestamp"].values[0]
    elVs = df_test["actualVelocity"].values
    elVelSpline = UnivariateSpline(elXs, elVs, s=0)
    elAccSpline = elVelSpline.derivative(n=1)

    return (elAccSpline, elXs, elVs)

def miniformat(df):
    """
    formatting date 
    """
    # Reiniciar el índice
    df.reset_index(inplace=True)
    # Asignar un nombre al índice
    df.index.name = "Axis"
    df = df.rename(columns={"index": "time"})
    print(df)
    df = str(df["time"][0])
    event = datetime.strptime(df, "%Y-%m-%d %H:%M:%S.%f%z").strftime(
        "%Y-%m-%dT%H:%M:%S.%f"
    )
    print()
    print("Event happened at: ", event)
    event = Time(event, scale="utc", format="isot")
    return event
